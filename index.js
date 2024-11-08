class Birthday {
    constructor(year, month, day) {
        this.year = year
        this.month = month
        this.day = day
    }

    toDate() {
        return new Date(this.year, this.month - 1, this.day)
    }

    next() {
        return new Birthday(this.year + 1, this.month, this.day)
    }

    prev() {
        return new Birthday(this.year - 1, this.month, this.day)
    }

}

class MannakaBirthday extends Birthday {
    constructor(birthday1, birthday2) {
        const mb = MannakaBirthday.mannakaBirthday(birthday1, birthday2)
        super(mb.year, mb.month, mb.day)
        this.birthday1 = new Birthday(birthday1.year, birthday1.month, birthday1.day)
        this.birthday2 = new Birthday(birthday2.year, birthday2.month, birthday2.day)

    }

    static mannakaDate(date1, date2) {
        return new Date(date1.getTime() + (date2 - date1) / 2)
    }

    static mannakaBirthday(birthday1, birthday2) {
        const md = MannakaBirthday.mannakaDate(birthday1.toDate(), birthday2.toDate())
        return new Birthday(md.getFullYear(), md.getMonth() + 1, md.getDate())
    }

    next() {
        return new MannakaBirthday(this.birthday2, this.birthday1.next())
    }

    prev() {
        return new MannakaBirthday(this.birthday2.prev(), this.birthday1)
    }

}

function nextNextMannakaBirthday(birthday1, birthday2, today) {
    const year = today.year
    let bd1 = new Birthday(year, birthday1.month, birthday1.day)
    let bd2 = new Birthday(year, birthday2.month, birthday2.day)
    if (bd1.toDate() > bd2.toDate()) {
        bd1, bd2 = bd2, bd1
    }
    let nextMB = new MannakaBirthday(bd1, bd2)
    if (today.toDate() - nextMB.toDate() > 0) {
        nextMB = nextMB.next()
    }
    const nextNextMB = nextMB.next()
    return [nextMB, nextNextMB]
}

// ページがロードされたときに、フォームの送信イベントをリッスンする
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("mannakaBirthdayForm")
    const nextMBDiv = document.getElementById("nextMB")
    const nextNextMBDiv = document.getElementById("nextNextMB")
    const birthday1Month = document.getElementById("birthday1Month")
    const birthday1Day = document.getElementById("birthday1Day")
    const birthday2Month = document.getElementById("birthday2Month")
    const birthday2Day = document.getElementById("birthday2Day")

    form.addEventListener("submit", function (event) {
        // フォームのデフォルト送信動作をキャンセル
        event.preventDefault()
        let today = new Date()
        today = new Birthday(today.getFullYear(), today.getMonth() + 1, today.getDate())

        const birthday1 = new Birthday(today.year, parseInt(birthday1Month.value), parseInt(birthday1Day.value))
        const birthday2 = new Birthday(today.year, parseInt(birthday2Month.value), parseInt(birthday2Day.value))
        console.log(birthday1Month.value)
        console.log(birthday1)
        console.log(birthday2)
        const nextNextResult = nextNextMannakaBirthday(birthday1, birthday2, today)
        const nextMB = nextNextResult[0]
        const nextNextMB = nextNextResult[1]
        const nextMBString = `${nextMB.year}年${nextMB.month}月${nextMB.day}日`
        const nextNextMBString = `${nextNextMB.year}年${nextNextMB.month}月${nextNextMB.day}日`

        nextMBDiv.textContent = `次の真ん中バースデーは${nextMBString}です`
        nextNextMBDiv.textContent = `次の次の真ん中バースデーは${nextNextMBString}です`
    })
})