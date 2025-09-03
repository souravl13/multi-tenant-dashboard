from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/tenants_db')

def get_conn():
    return psycopg2.connect(DATABASE_URL)

def get_tenants():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, users, active FROM tenants ORDER BY id")
    rows = cur.fetchall()
    tenants = []
    for row in rows:
        tenants.append({
            "id": row[0],
            "name": row[1],
            "users": row[2],
            "active": row[3],
            "chart": [max(0, row[3] + i*2 - row[0]) for i in range(5)]
        })
    cur.close()
    conn.close()
    return tenants

@app.route('/')
def dashboard():
    tenants = get_tenants()
    return render_template("index.html", tenants=tenants)

@app.route('/tenants')
def tenants_page():
    tenants = get_tenants()
    return render_template("tenants.html", tenants=tenants)

@app.route('/add', methods=['GET', 'POST'])
def add_tenant():
    if request.method == 'POST':
        name = request.form['name']
        users = int(request.form['users'])
        active = int(request.form['active'])
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO tenants (name, users, active) VALUES (%s, %s, %s)", (name, users, active))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('tenants_page'))
    return render_template("add_tenant.html")

@app.route('/delete/<int:tenant_id>')
def delete_tenant(tenant_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM tenants WHERE id=%s", (tenant_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('tenants_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
