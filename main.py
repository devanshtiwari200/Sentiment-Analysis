from flask import Flask, request,render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app=Flask(__name__)


  

@app.route('/',methods=["GET","POST"])
def main():
    
    if request.method == "POST":
        inp= request.form.get('inp')
          #object for vadersentiment
        sent_obj=SentimentIntensityAnalyzer()
        # using popularity_score method 
        sent_score=sent_obj.polarity_scores(inp)
        if sent_score['compound']>= 0.05:
            return render_template('homepage.html',message="Positive")
        elif sent_score['compound'] <= -0.05:
            return render_template('homepage.html',message="Negative")
        
        else:
            return render_template('homepage.html',message="Neutral")
        return render_template("homepage.html")
    
if __name__ == '__main__':
    app.run(debug=True)
