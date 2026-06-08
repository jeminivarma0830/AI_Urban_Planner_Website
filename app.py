from flask import Flask, render_template, request
import random
app=Flask(__name__)

def generate_city(size,r,c,p,s,h):
    grid=[['Road' for _ in range(size)] for _ in range(size)]
    zones=[('Residential',r),('Commercial',c),('Park',p),('School',s),('Hospital',h)]
    for zone,count in zones:
        placed=0
        while placed<count:
            x=random.randint(0,size-1); y=random.randint(0,size-1)
            if grid[x][y]=='Road':
                grid[x][y]=zone; placed+=1
    return grid

@app.route('/',methods=['GET','POST'])
def home():
    grid=None
    if request.method=='POST':
        size=int(request.form['size'])
        grid=generate_city(size,int(request.form['residential']),int(request.form['commercial']),int(request.form['parks']),int(request.form['schools']),int(request.form['hospitals']))
    return render_template('index.html',grid=grid)

if __name__=='__main__':
    app.run(debug=True)
