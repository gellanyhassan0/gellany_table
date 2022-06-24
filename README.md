# gellany_table

app help to web scraping many kind of tables inside html static or dynamic response as send keyword to serach box and getting results 

<code>python3 gellany_table.py --url "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)" --table "1"</code><br>
<code>python3 gellany_table.py --url = "https://www.thesun.co.uk/sport/football/"  --element = '//div[@class="teaser__copy-container"]' --search = "s" --key = "goals" </code><br>

# docker deploy
#/home/go/ = your path your already download git folder in it<br>
  
<code>docker image build -t gellany_table /home/go/gellany_table --no-cache</code><br>
<code>docker run --publish 4444:4444 -it -d gellany_table</code><br>
<code>docker ps</code><br>
<code>docker exec -it 83ea954d9b5a python3 gellany_table.py --url "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)" --table "1"</code><br>



<code>docker stop f77d93571bcc</code><br>
<code>docker ps</code><br>


# docker pull direct
#/home/go/ = your path your already download git folder in it<br>
<code>docker pull gellany/gellany_table</code><br>
<code>docker run --publish 4000:4000 -it -d gellany/gellany_table</code><br>
<code>docker ps</code><br>
<code>docker exec -it 83ea954d9b5a python3 gellany_table.py --url "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)" --table "1"</code><br>
<code>docker stop f77d93571bcc</code><br>


# docker push
<code>docker login --username username</code><br>
<code>docker image list</code><br>
<code>docker tag a2ac10640f5b gellany/gellany_table</code><br>
<code>docker push gellany/gellany_table:latest</code><br>

# docker image list removed
<code>docker images rm </code><br>

# docker image remove all
<code>docker image list|awk '{print $3}'|xargs -I z docker rmi --force z</code><br>
<code>docker image list</code><br>

# docker system Remove unused data
<code>docker system prune --force</code><br>
  
# docker check and delete volume 
<code>docker system df</code><br>
<code>docker system prune</code><br>


