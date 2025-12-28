import axios from axios;

const SERVER_URL = "localhost://128.0.0.8000/"

const register = async(data)=>{
    try{
        const res = await axios.post(`${SERVER_URL}/auth/register`,
            {params: {data}}
        );
        return res;
    }
    catch (error){
        return error;
    };
};


const login = async(data)=>{
    try {
        const res = await axios.post(`${SERVER_URL}/auth/login`,
            {params: {data}}
        );
        return res;
    } catch (error) {
        return error;
    }
};



const getProfile = async (userId)=>{
    try {
        const res = await axios.get(`${SERVER_URL}/auth/profile`, 
            {params: {"userId": userId}}
        );
        return res;
    } catch (error) {
        return error;
    }
};
