import React from "react"

class AddUser extends React.Component {
    userAdd = {}
    constructor(props) {
        super(props)
        this.state = {
            first_name: "",
            last_name: "",
            avatar: "",
            bio: "",
            age: 1,
            isHappy: false
        }
    }
    render() {
        return (
            <form ref={(el) => this.myForm = el} className="white-table">
                <input placeholder="Имя" className="white-input" onChange={(e) => this.setState({ first_name: e.target.value })} />
                <input placeholder="Фамилия" className="white-input" onChange={(e) => this.setState({ last_name: e.target.value })} />
                <input placeholder="Вставьте URL картинки" className="white-input" onChange={(e) => this.setState({ avatar: e.target.value })} />
                <textarea placeholder="Биография" className="white-textarea" onChange={(e) => this.setState({ bio: e.target.value })}></textarea>
                <input placeholder="Возраст" className="white-textarea" onChange={(e) => this.setState({ age: e.target.value })} />
                <label htmlFor="isHappy">Счастлив?</label>
                <input type="checkbox" id="isHappy" onChange={(e) => this.setState({ isHappy: e.target.checked })} />
                <button type="button" onClick={() => {
                    this.myForm.reset()
                    this.userAdd = {
                        first_name: this.state.first_name,
                        last_name: this.state.last_name,
                        avatar: this.state.avatar,
                        bio: this.state.bio,
                        age: this.state.age,
                        isHappy: this.state.isHappy,
                    }
                    if (this.props.user)
                        this.userAdd.id = this.props.user.id
                    this.props.onAdd(this.userAdd)
                }
                }>Добавить</button>
            </form>
        )
    }
}

export default AddUser