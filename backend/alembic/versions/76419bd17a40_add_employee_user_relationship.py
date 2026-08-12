"""add employee user relationship

Revision ID: 76419bd17a40
Revises:
Create Date: 2026-08-12 16:22:18.775983
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "76419bd17a40"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # ---------------------------------------------------------
    # Attendance constraints
    # ---------------------------------------------------------

    op.alter_column(
        "attendances",
        "early_leave_status",
        existing_type=sa.VARCHAR(length=20),
        nullable=False,
        existing_server_default=sa.text("'NO'::character varying"),
    )

    op.alter_column(
        "attendances",
        "attendance_status",
        existing_type=sa.VARCHAR(length=20),
        nullable=False,
        existing_server_default=sa.text("'PRESENT'::character varying"),
    )

    # Change attendance.employee_id -> employees.id
    op.drop_constraint(
        "attendances_employee_id_fkey",
        "attendances",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "attendances_employee_id_fkey",
        "attendances",
        "employees",
        ["employee_id"],
        ["id"],
    )

    # ---------------------------------------------------------
    # Employee -> User relationship
    # ---------------------------------------------------------

    # First add nullable column because employees table
    # may already contain data.
    op.add_column(
        "employees",
        sa.Column("user_id", sa.Integer(), nullable=True),
    )

    # ---------------------------------------------------------
    # IMPORTANT:
    # Populate employee.user_id before making it NOT NULL.
    #
    # If employee.id corresponds to users.id in your existing
    # database, this is enough.
    # ---------------------------------------------------------

    op.execute(
        """
        UPDATE employees
        SET user_id = id
        WHERE user_id IS NULL
        """
    )

    # Now make it NOT NULL
    op.alter_column(
        "employees",
        "user_id",
        existing_type=sa.Integer(),
        nullable=False,
    )

    # Unique + FK
    op.create_unique_constraint(
        "uq_employees_user_id",
        "employees",
        ["user_id"],
    )

    op.create_foreign_key(
        "fk_employees_user_id_users",
        "employees",
        "users",
        ["user_id"],
        ["id"],
    )

    # ---------------------------------------------------------
    # users.role VARCHAR -> PostgreSQL ENUM
    # ---------------------------------------------------------

    role_enum = sa.Enum(
        "ADMIN",
        "TEACHER",
        "USER",
        name="role",
    )

    # Create enum type first
    role_enum.create(op.get_bind(), checkfirst=True)

    # Convert existing VARCHAR values to ENUM
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN role TYPE role
        USING role::text::role
        """
    )


def downgrade() -> None:

    # ---------------------------------------------------------
    # users.role ENUM -> VARCHAR
    # ---------------------------------------------------------

    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN role TYPE VARCHAR(30)
        USING role::text
        """
    )

    role_enum = sa.Enum(
        "ADMIN",
        "TEACHER",
        "USER",
        name="role",
    )

    role_enum.drop(op.get_bind(), checkfirst=True)

    # ---------------------------------------------------------
    # Employee -> User relationship
    # ---------------------------------------------------------

    op.drop_constraint(
        "fk_employees_user_id_users",
        "employees",
        type_="foreignkey",
    )

    op.drop_constraint(
        "uq_employees_user_id",
        "employees",
        type_="unique",
    )

    op.drop_column(
        "employees",
        "user_id",
    )

    # ---------------------------------------------------------
    # Attendance FK
    # ---------------------------------------------------------

    op.drop_constraint(
        "attendances_employee_id_fkey",
        "attendances",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "attendances_employee_id_fkey",
        "attendances",
        "employees",
        ["employee_id"],
        ["id"],
    )

    # ---------------------------------------------------------
    # Nullable attendance fields
    # ---------------------------------------------------------

    op.alter_column(
        "attendances",
        "attendance_status",
        existing_type=sa.VARCHAR(length=20),
        nullable=True,
        existing_server_default=sa.text("'PRESENT'::character varying"),
    )

    op.alter_column(
        "attendances",
        "early_leave_status",
        existing_type=sa.VARCHAR(length=20),
        nullable=True,
        existing_server_default=sa.text("'NO'::character varying"),
    )