import { useEffect, useState } from "react";
import { getEmployees, createEmployee } from "../../services/employeeService";

import EmployeeModal from "../../components/ui/EmployeeModal";

import EmployeeForm from "../../pages/employee/EmployeeForm";



function EmployeeList() {


    const [employees,setEmployees] = useState([]);

    const [openModal,setOpenModal] = useState(false);

    const [loading, setLoading] = useState(false);



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

        await createEmployee(formData);

        setOpenModal(false);

        loadEmployees();

    } catch (error) {

        console.error(error);

    } finally {

        setLoading(false);

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

                    onClick={()=>setOpenModal(true)}

                    className="
                        bg-cyan-500
                        px-5
                        py-3
                        rounded-xl
                        text-white
                        font-semibold
                    "

                >

                    + Add Employee

                </button>


            </div>




            <div className="
                bg-white/5
                rounded-2xl
                overflow-hidden
            ">


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

                            </tr>


                        ))

                    }


                    </tbody>


                </table>


            </div>





            <EmployeeModal
    open={openModal}
    title="Add Employee"
    onClose={() => setOpenModal(false)}
>
    <EmployeeForm
        onSubmit={handleCreateEmployee}
        loading={loading}
    />
</EmployeeModal>




        </div>

    );

}


export default EmployeeList;