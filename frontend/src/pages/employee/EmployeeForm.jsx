import { useState } from "react";

function EmployeeForm({ onSubmit, loading }) {

    const [form, setForm] = useState({
        employee_code: "",
        first_name: "",
        last_name: "",
        email: "",
        phone: "",
        department: "",
        designation: "",
        joining_date: "",
        status: "ACTIVE"
    });

    function handleChange(e) {

        setForm({
            ...form,
            [e.target.name]: e.target.value
        });

    }

    function handleSubmit(e) {

        e.preventDefault();

        onSubmit(form);

    }

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-5"
        >

            <input
                name="employee_code"
                placeholder="Employee Code"
                value={form.employee_code}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                name="first_name"
                placeholder="First Name"
                value={form.first_name}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                name="last_name"
                placeholder="Last Name"
                value={form.last_name}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                name="email"
                placeholder="Email"
                value={form.email}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                name="phone"
                placeholder="Phone"
                value={form.phone}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                name="department"
                placeholder="Department"
                value={form.department}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                name="designation"
                placeholder="Designation"
                value={form.designation}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <input
                type="date"
                name="joining_date"
                value={form.joining_date}
                onChange={handleChange}
                className="w-full p-3 rounded-xl bg-slate-900 border border-slate-700"
            />

            <button
                type="submit"
                disabled={loading}
                className="w-full bg-cyan-500 hover:bg-cyan-600 rounded-xl py-3 font-bold"
            >
                {loading ? "Saving..." : "Save Employee"}
            </button>

        </form>

    );

}

export default EmployeeForm;