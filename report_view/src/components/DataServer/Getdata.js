import React, {Component} from 'react';
import './Getdata.css';

class GetData extends Component {
    constructor(props){
        super(props);
        this.state = {
            error : null,
            isLoaded : false,
            posts : []        
        };
    }

    componentDidMount() {
        // Pick up colect from the Flask Api
        // this return the table
        fetch("/report")
        .then( response => response.json())
        .then(
            // handle the result
            (result) => {
                this.setState({
                    isLoaded : true,
                    posts : result.result
                });
            },

            // Handle error 
            (error) => {
                this.setState({
                    isLoaded: true,
                    error
                })
            },
        )
    }


    render() {
        const {error, isLoaded, posts} = this.state;

        if(error){
            return <div>Error in loading</div>
        }else if (!isLoaded) {
            return <div>Loading ...</div>
        }else{
            return(
                <div>
                    <table>
                        <thead>
                        <tr>
                            <th>ID</th>
                            <th>Timestamp</th>
                            <th>Temperature</th>
                            <th>Duration</th>
                        </tr>
                        </thead>
                        <tbody>
                        {
                            posts.map(post => (
                                <tr>
                                    <td>{post.id}</td>
                                    <td>{post.timestamp}</td>
                                    <td>{post.temperature}</td>
                                    <td>{post.duration}</td>
                                </tr>
                            ))
                        }
                        </tbody>
                    </table>
                </div>
            );
        }    
    }
}

export default GetData;
