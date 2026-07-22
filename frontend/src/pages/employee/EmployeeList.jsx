import { useEffect, useState } from "react";
import { getEmployees, createEmployee, updateEmployee, deleteEmployee } from "../../services/employeeService";

import EmployeeModal from "../../components/ui/EmployeeModal";

import EmployeeForm from "../../pages/employee/EmployeeForm";

import { Menu, MenuButton, MenuItems, MenuItem } from "@headlessui/react";

import { EllipsisVertical, Pencil, Trash2, Eye } from "lucide-react";



function EmployeeList() {


    const [employees,setEmployees] = useState([]);

    const [openModal,setOpenModal] = useState(false);

    const [loading, setLoading] = useState(false);

    const [selectedEmployee, setSelectedEmployee] = useState(null);

    const editEmployee = (employee) => { setSelectedEmployee(employee);setOpenModal(true);
    };



    useEffect(()=>{

        loadEmployees();

    },[]);



    const loadEmployees = async()=>{

        try{

            const data = await getEmployees();

            setEmployees(data);

        }
        catch(error){

            console.log(error);

        }

    };

    const handleCreateEmployee = async (formData) => {

    try {

        setLoading(true);

        if (selectedEmployee) {

            await updateEmployee(

                selectedEmployee.id,

                formData

            );

        } else {

            await createEmployee(formData);

        }

        setOpenModal(false);

        setSelectedEmployee(null);

        loadEmployees();

    } catch (error) {

        console.error(error);

    } finally {

        setLoading(false);

    }

};

    const handleDeleteEmployee = async (employeeId) => {

    const confirmDelete = window.confirm(
        "Are you sure you want to delete this employee?"
    );

    if (!confirmDelete) {

        return;

    }

    try {

        await deleteEmployee(employeeId);

        loadEmployees();

    } catch (error) {

        console.error(error);

    }

};
    return (

        <div>
            <div className="
                flex
                justify-between
                items-center
                mb-6
            ">
                <h1 className="
                    text-3xl
                    font-bold
                ">
                    Employees
                </h1>

                <button
                    onClick={() => {
                        setSelectedEmployee(null);
                        setOpenModal(true);
                    }}
                    className=" bg-cyan-500 px-5 py-3 rounded-xl text-white font-semibold">
                    + Add Employee
                </button>
            </div>
            <div className="bg-white/5 rounded-2xl overflow-hidden">
                <table className="w-full">
                    <thead>
                        <tr className="border-b border-white/10">

                            <th className="p-4 text-left">
                                ID
                            </th>

                            <th className="p-4 text-left">
                                Name
                            </th>

                            <th className="p-4 text-left">
                                Email
                            </th>

                            <th className="p-4 text-left">
                                Phone
                            </th>

                            <th className="p-4 text-left">
                                Designation
                            </th>

                            <th className="p-4 text-left">
                                Action
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                    {
                        employees.map((emp)=>(
                            <tr
                                key={emp.id}
                                className="border-b border-white/10">
                                <td className="p-4">
                                    {emp.id}
                                </td>

                                <td className="p-4">
                                    {emp.first_name}
                                </td>

                                <td className="p-4">
                                    {emp.email}
                                </td>

                                <td className="p-4">
                                    {emp.phone}
                                </td>

                                <td className="p-4">
                                    {emp.designation}
                                </td>
<td className="p-4">

    <Menu as="div" className="relative inline-block text-left">

        <MenuButton
            className="
                p-2
                rounded-lg
                hover:bg-slate-700
                transition
            "
        >

            <EllipsisVertical size={20} />

        </MenuButton>

        <MenuItems
            anchor="bottom end"
            className="
                w-48
                rounded-xl
                bg-slate-900
                border
                border-slate-700
                shadow-2xl
                p-2
                focus:outline-none
                z-50
            "
        >

            <MenuItem>

                {({ active }) => (

                    <button
                        onClick={() => editEmployee(emp)}
                        className={`
                            flex
                            w-full
                            items-center
                            gap-3
                            rounded-lg
                            px-4
                            py-3
                            ${
                                active
                                    ? "bg-slate-700"
                                    : ""
                            }
                        `}
                    >

                        <Pencil
                            size={18}
                            className="text-yellow-400"
                        />

                        Edit

                    </button>

                )}

            </MenuItem>

            <MenuItem>

                {({ active }) => (

                    <button
                        className={`
                            flex
                            w-full
                            items-center
                            gap-3
                            rounded-lg
                            px-4
                            py-3
                            ${
                                active
                                    ? "bg-slate-700"
                                    : ""
                            }
                        `}
                    >

                        <Eye
                            size={18}
                            className="text-cyan-400"
                        />

                        View

                    </button>

                )}

            </MenuItem>

            <MenuItem>

                {({ active }) => (

                    <button
                        onClick={() => handleDeleteEmployee(emp.id)}
                        className={`
                            flex
                            w-full
                            items-center
                            gap-3
                            rounded-lg
                            px-4
                            py-3
                            text-red-400
                            ${
                                active
                                    ? "bg-red-500/20"
                                    : ""
                            }
                        `}
                    >

                        <Trash2 size={18} />

                        Delete

                    </button>

                )}

            </MenuItem>

        </MenuItems>

    </Menu>

</td>
                            </tr>
                        ))
                    }
                    </tbody>
                </table>
            </div>

            <EmployeeModal
                open={openModal}
                title={selectedEmployee ? "Edit Employee" : "Add Employee"}
                onClose={() => setOpenModal(false)}
            >
                <EmployeeForm
                    employee={selectedEmployee}
                    onSubmit={handleCreateEmployee}
                    loading={loading}
                />
            </EmployeeModal>
        </div>

    );
}

export default EmployeeList;