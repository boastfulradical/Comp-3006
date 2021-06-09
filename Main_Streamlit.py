import seaborn as sns
import sys
import time
import os
from streamlit import cli as stcli
import streamlit as st
import pandas as pd
import altair as alt
import requests
import io
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
import matplotlib.dates as mdates



def main():

    st.title('Wehrmacht Deaths During World War II')
    st.write('\n')
    img = Image.open("Soldiers_in_Paris.jpg")
    st.image(img, caption = "Wehrmacht Soldiers on Parade in Paris")

    st.subheader('Wehrmacht Overview')
    st.write('During World War II, over 17 million Germans fought for the Third Reich. The vast majority of '
             'these men fought under the Wehrmacht, or the Armed Forces of Nazi Germany. The Wehrmacht '
             'was active in nearly every corner of Europe from western France to the river Volga in Russia; '
             'from Sicily to Narvik in Norway. They were responsible for death and destruction on a scale '
             'never seen before.')

    st.write("Through the _Heer_, or Army, the Wehrmacht conducted immense ground campaigns and operations. "
             "They started the war with the Invasion of Poland in September 1939 and were combat effective "
             "until the very end during the 9th Army's breakout from the Halbe Kessel in late April 1945. "
             "Despite their intimidating presence and military accomplishments, the _Heer_ suffered immense "
             "deaths and losses throughout the war. By war's end, over 4.2 million men who served with the "
             "Heer would be killed. ")

    st.write("Fighting alongside the Heer was the Waffen-SS. Comprised of mostly volunteer recruits, many of "
             "them foreigners, they would form an elite fighting unit. Waffen-SS units were similar to the "
             "SS as they did follow the political ideology of Nazi's. Their commitment to Nazism and hatred "
             "of communism made the Waffen-SS an especially feared force to encounter. Often, they were thrown "
             "into the thickest battles and suffered tremendous losses because of this. Despite being the first "
             "to receive new weapons and equipment, the loss rate of Waffen-SS units was some of the highest "
             "suffered by any organization in the Wehrmacht. Over 313,000 men would die fighting under the "
             "Waffen-SS.")

    st.markdown('**Waffen-SS units engaged in combat: ** ')
    video_file = open('Waffen-SS Combat.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time = 61)

    st.write('\n')

    st.write("The _Kriegsmarine_, or Navy, was critical in defending the Third Reich's shore and projecting "
             "power across the sea. The U-boat fleet nearly brought Great Britain to her knees in the early "
             "years of the war. However, the surface fleet of capital ships like the Bismarck and Tirpitz "
             "failed to be combat effective as they were either sunk or kept in port. The _Kriegsmarine's_ "
             "effectiveness gradually declined throughout the war and would later be used mostly as means "
             "to evacuate civilians and soldiers from the East back to Germany. By the end of the war "
             "nearly 140,000 men died serving with the _Kriegsmarine_, mostly in the U-boat fleet. ")

    st.write("Controlling the skies in the opening days of the Second World War was the _Luftwaffe_, or Air "
             "Force of the Third Reich. Commanded by _Reichsmarschall_ Hermann Goring, the _Luftwaffe_ was the "
             "spearhead of the Wehrmacht. Sent to soften and terrorize targets into submission, their  "
             "effectiveness was unquestionable. Possessing a mix of obsolete and state-of-the-art aircraft "
             "and technologies, all enemies respected the _Luftwaffe_ and her abilities. However, as the war "
             "progressed, experienced and irreplaceable pilots were killed and aircraft were lost. By 1944, "
             "the once feared _Luftwaffe's_ wings had been clipped and German cities were being pounded into "
             "oblivion by the American and Royal air forces and Germany's ground forces were left vulnerable to "
             "Allied air power. Over 430,000 men would die by the end of the war serving with the _Luftwaffe_. ")


    st.subheader('All Roads Lead to War')
    img = Image.open("Nuremberg_Rally.jpg")
    st.image(img, caption = "Pre-war Nazi Rally at Nuremberg Whose Purpose was to Demonstrate Germany's Rising Power")

    st.write("On January 30, 1933, after over a decade of violent and non-violent attempts to overthrow the "
             "government, Adolf Hitler and his Nazi party were elected by the German people to a majority of "
             "seats in the _Reichstag_, or German parliament. Being elected Chancellor, Hitler "
             "now had the authority to build the Germany he wanted. Shortly after his rise, "
             "Hitler began to implement his racial laws against the Jews and started to consolidate his power. ")

    st.write("One of the most important events in Hitler's consolidation of power is the _Night of the Long Knives_. "
             "Fearing that Ernst Rohm, the head of the _Sturmabteilung_ or SA (the Nazi paramilitary organization), "
             "would stage a coup against the _Reichswehr_, currently Germany's Armed Forces; Hitler and other top "
             "Nazi's planned an extrajudicial assassinations of Rohm and other SA leaders. Between June 30th to "
             "July 2nd, 1934, at least 85 SA leaders were killed. The result of the _Night of the Long Knives_ "
             "had a profound impact on Nazi Germany. Firstly, the SA was all but eliminated after the event, "
             "securing the _Reichswehr_ as Germany's official military arm. Additionally, German courts legally "
             "sanctioned the assassinations afterwards giving Hitler and the Nazi's even greater legal rights "
             "and privileges which opened the door for greater atrocities later on. ")

    img = Image.open("Rohm and Hitler.jpg")
    st.image(img, caption = "Hitler and Rohm")

    st.write("As Hitler consolidated his powers, the armaments industry in Germany took off under the Nazi "
             "leadership. On March 16th, 1935, Hitler openly rejected all terms and restrictions within the "
             "Treaty of Versailles. National conscription was announced and the buildup of the _Reichswehr_ had "
             "officially begun. On May 21st, 1935, _Reichswehr_ was officially dropped in favor of Wehrmacht. "
             "All new soldiers to the Wehrmacht had to pledge a personal oath to Adolf Hitler, not Germany. "
             "It becomes clear the Wehrmacht is not the military arm of Germany, but rather of Hitler himself. "
             "Men were quickly drafted into service and soon the armed forces of Germany that was restricted "
             "to just 100,000 men would balloon to over three million by the start of the war.")

    st.write("With Germany's military might growing, Hitler aimed outside of his borders for more land. Hitler, "
             "seeing that Germany needed more room to expand, adopted the policy of _Lebensraum_. The core "
             "principal of _Lebensraum_ is that Germany needed more 'living space' for its people. That territory "
             "had to come from conquered lands where first lands to fall was Austria with the _Anschulss_. "
             "Strictly forbidden under the Treaty of Versailles, the union between Germany and Austria took "
             "effect on March 12, 1938 after Germany's annexation. Without a shot being fired, Hitler captured "
             "Austria. A few months later, on September 30, 1938, Germany annexed the _Sudetenland_ (territory "
             "that held mostly ethnic and German speakers) from Czechoslovakia. In March of 1939, Germany "
             "annexed the rest of the country. ")

    st.write("Hitler's aggression was growing. Rearmament had taken Germany from being a non-power to a regional "
             "hegemon. On 23rd of August 1939, the final act before war happened. The world thought that "
             "fascist Germany and the communist Soviet Union would never be friends, but on this day they "
             "signed the Molotov-Ribbentrop Pact. Outwardly, it was a non-aggression pact between the two dictators, "
             "however, the pact also divided Eastern Europe between the two. By the end of August 1939, Germany "
             "was ready for war. ")

    st.write("Little did the people of Germany know how much devastation Hitler's own armies would bring upon "
             "themselves or all the suffering they'd experience.")

    st.subheader('Wehrmacht Recruitment')
    img = Image.open("Wehrmacht Soldiers.jpg")
    st.image(img, caption = 'Wehrmacht Soldiers on the March')

    st.write("During normal times, the standard age of conscription and recruitment into the Wehrmacht was 18-45 "
             "years old, with most being around 20 years old. However, as the war progressed and the conditions "
             "of the Wehrmacht and within Germany itself began to deteriorate, the need for more soldiers grew "
             "increasingly desperate. Founded in October 1944, the _Volksstrum_, or 'People's Storm' was raised. "
             "Originally, the _Volksstrum_ was to expand the age of military service to boys as young as 16 and "
             "men as old as 60. However, in reality, boys as young as 13 and men older than 65 were called "
             "up to fight for the dying Reich.")

    st.write("The following charts and tables present recruitment information for Wehrmacht servicemen based on "
             "their year of birth. ")

    st.markdown('**Servicemen who joined the Wehrmacht by year of birth:  ** ')
    df = st.cache(pd.read_csv)('Wehrmacht_Members_1.csv')
    st.write(df)


    birthYear = ['1873', '1875', '1877', '1878', '1879', '1881', '1882', '1884', '1885', '1886', '1887', '1888', '1889',
                 '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898', '1899', '1900', '1901', '1902',
                 '1903', '1904', '1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915',
                 '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928']
# count = 52
    birthCount = [248, 3773, 4699, 3773, 496, 8720, 4021, 16844, 16944, 15918, 26242,
                  11815, 28989, 34036, 34432, 49688, 44759, 88096, 90943, 115681, 194049, 200196,

                 212124, 265250, 236614, 294365, 282138, 302108, 388396, 567205, 566100, 671240, 679837,
                 736220, 698654, 746206, 793114, 858017, 671606, 499856, 447510, 458801, 689658, 931123,
                 918258, 735183, 725170, 696996, 578926, 382457, 223827, 43833]

    birthDeaths = [0, 0, 0, 2033, 0, 2000, 1000, 4033, 5033, 5033, 4033, 3033, 10132,
               6033, 7066, 5033, 8099, 20165, 9000, 25198, 17033, 39297, 41330, 73726, 67627, 99759,
               84660, 92825, 94858, 152287, 157221, 204452, 187353, 221650, 225551, 226683, 211221, 269881, 193353,
               133825, 122627, 149858, 229287, 318848, 276419, 240419, 269749, 271716, 235683, 153188, 105990, 32231]

    recYear =  ['Pre-1939', '1939', '1940',  '1941',    '1942',   '1943',   '1944',   '1945']
    recMonth = [1146141,    3527538, 4109298, 2507457,  2465628,  2005653,  1308096,  225343]
    recCumm =  [1146141,    4673679, 8782977, 11290434, 13756062, 15761715, 17069811, 17295154]


    # Plotting Wehrmacht recruitment and deaths by birth year
    fig1 = go.Figure(data=[go.Bar(name='Count', x=birthYear, y=birthCount),
                           go.Bar(name='Deaths',x=birthYear, y=birthDeaths)])
    fig1.update_xaxes(title_text="Year")
    fig1.update_yaxes(title_text="Count in Millions")
    fig1.update_layout(barmode='group', title = '<b>Wehrmacht Recruitment and Deaths by Birth Year</b>')
    st.plotly_chart(fig1)


    st.markdown(""" #### Interesting Notes on the Recruitment Data: 

    - Most servicemen were born between 1905 to 1925, with an age at the start of the war falling 
            in between 14 and 34 years old. This age group holds the men that are most physically able to fight 
            either immediately, or in a few years. Though the records and data stop being available for those 
            born past 1928, many boys born after that did serve in the _Volksstrum_.  
            
    - The data ends recruitment birth years at 1928. Those born in 1928 would have be 16 or 17 years old in 1944 
            or 1945 when they would have joined. Records for those who are younger than that were not available
            in the data source. Record keeping in the Wehrmacht started to breakdown as Germany itself began to
            collapse as 1944 turned to 1945. 
    
    - There is a very noticeable and substantial drop in recruits born from 1915 to 1918. Even those the men 
            born in this birth range would've been perfectly able to fight, they didn't. One of the most 
            obvious reasons for this is that their fathers were fighting and dying for the Kaiser in the 
            trenches of the First World War.  
            
    """)



    img = Image.open("Volksstrum Boys Captured by US 6th Armored Division.jpg")
    st.image(img, caption = 'Volksstrum Boys Captured by the US 6th Armored Division - 1945')


    st.markdown("**Recruitment and Deaths of Wehrmacht members by birth group: **")
    df1 = st.cache(pd.read_csv)('Birth_Groups.csv')
    st.write(df1)

    birthGroup = ['Pre-1900', '1900-1904', '1905-1909', '1910-1914', '1915-1919', '1920-1924', '1925-1928']
    groupMember = [1206486, 1380475, 2872778, 3832211, 2767431, 4006730, 1229043]
    groupDeaths = [214584, 418597, 796171, 1154986, 828950, 1377151, 527092]

    fig4 = go.Figure(data=[go.Bar(name='Count', x=birthGroup, y=groupMember),
                           go.Bar(name='Deaths',x=birthGroup, y=groupDeaths)])
    fig4.update_yaxes(title_text="Count in Millions")
    fig4.update_xaxes(title_text="Birth Group")
    fig4.update_layout(barmode='group', title = '<b>Wehrmacht Recruitment and Deaths by Birth Group</b>')
    st.plotly_chart(fig4)



    st.write("With Hitler re-instating conscription in 1935, the number of servicemen in the Wehrmacht  "
             "quickly grew. By the end of 1939, over 3.5 million men had joined the Armed Forces. Many "
             "recruits were foreign volunteers convinced to join the Wehrmacht to fight against Germany's "
             "enemies. After the fall of France in June 1940, Germany began to build up for the invasion "
             "of the Soviet Union. By June 1941, on the eve of Operation Barbarossa being launched, the "
             "Wehrmacht reached its peak strength. ")

    st.write("However, as the war progressed, the pool of available manpower started to dry up. Qualified "
             "fresh recruits became increasingly rare to come across. The largest and best pool of available "
             "manpower the Wehrmacht could draw from as the was progressed was wounded soldiers. Wounded "
             "men returned to service at a rate of about 50%. However, these men would often be sent to static "
             "divisions in defense positions as they were not as mobile as their unwounded comrades.  ")

    st.markdown("**Annual and Cumulative Wehrmacht Recruitment: **")
    df2 = st.cache(pd.read_csv)('Wehrmacht_Recruitment.csv')
    st.write(df2)

    # Plotting Annual and Cumulative Wehrmacht recruitment
    fig = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
    fig.add_trace(go.Bar(x=recYear, y=recMonth, name="Annual"), secondary_y=False)
    fig.add_trace(go.Scatter(x=recYear, y=recCumm, name="Cumulative"), secondary_y=True)
# Add figure title
    fig.update_layout(title_text="<b>Annual and Cumulative Wehrmacht Recruitment</b>")
# Set x-axis title
    fig.update_xaxes(title_text="Year")
# Set y-axes titles
    fig.update_yaxes(title_text="Wehrmacht Annual Recruitment", secondary_y=False)
    fig.update_yaxes(title_text="Cumulative Recruitment", secondary_y=True)

    st.plotly_chart(fig)

    st.write("The vast majority of recruits to the Wehrmacht served with the _Heer_. The _Heer's_ importance "
             "and demand for personnel cannot be understated.   ")

    st.markdown('**Total recruitments and deaths of major Wehrmacht organizations:  ** ')
    df = st.cache(pd.read_csv)('Primary_Branches.csv')
    st.write(df)


    branch = ['Heer', 'Waffen-SS', 'Luftwaffe', 'Kriegsmarine']
    member = [12701665, 900000, 2499868, 1193621]
    branchDead = [4202030, 313749, 432706, 138429]

    fig2 = go.Figure(data=[go.Bar(name='Member', x=branch, y=member),
                           go.Bar(name='Deaths', x=branch, y=branchDead)])
    fig2.update_yaxes(title_text="Count in Millions")
    fig2.update_xaxes(title_text="Wehrmacht Organization")
    fig2.update_layout(barmode='group', title = '<b>Wehrmacht Recruitment and Deaths by Major Organization</b>')
    st.plotly_chart(fig2)


###     END WITH RECRUITMENT PORTION    ###
###     START OF PART 3, THE DEATHS AND LOSSES      ###

    st.subheader('**Overview of Wehrmacht Deaths and Losses**')
    img = Image.open('Poland_Hitler.jpg')
    st.image(img, caption = 'Hitler watching his soldiers march into Poland, September 1939')

    st.write("On the morning of September 1st, 1939, German forces entered Poland and Europe would "
             "be plunged into war. As Hitler's armies rolled through Poland the world did little "
             "except watch. Soon after the invasion, Great Britain and France would declare war "
             "on Germany and the Second World War would begin.")

    st.write("The success Germany had in the early days of the war is undeniable. Annihilating Poland "
             "in about a months time and then smashing through Belgium, Norway, Denmark, and France "
             "in a matter of weeks. However, with the failure of removing the British from the war, "
             "Germany would find herself soon fighting a substantially more challenging multi-front "
             "conflict.")

    st.write("Wehrmacht deaths and losses in these early years were fairly minimal. Once Operation "
             "Barbarossa was launched, the deaths began to spike. The Soviet Union was a totally different "
             "adversary than the Poles or French. Even though the Soviets took immense losses during "
             "the first months of invasion, her land and population allowed her to absorb these losses. ")

    st.write("Failing to capture Moscow in December 1941, Wehrmacht deaths would not fall back down. "
             "They would stay at elevated levels for the remainder of the war and by the end of 1943, "
             "Germany was unable to adequately replace her losses in both men and machines.")

    st.write("After the successful Allied landings at Normandy with Operation Overlord and the successful "
             "breakout under Operation Cobra, the fate of Nazi Germany was all but sealed. Suffering from "
             "the colossal defeats in Normandy and in Poland from Operation Bagration, the Wehrmacht was "
             "reeling. Despite struggling to find the men, machines, or fuel to keep the fight sustained "
             "or fronts stable, Hitler gambled massively with his remaining valuable panzer, mechanized "
             "infantry, and Luftwaffe reserves with the Ardenness Counteroffensive in December in 1944 in "
             "an attempt to size the port of Antwerp and negotiate a peace with the western powers. ")

    st.write("After the brazen offensive failed, Germany found itself unable to resist the immense pressure "
             "from the Allied powers. Despite its man power quickly draining, its tanks and and fighters "
             "without fuel, and little food to feed civilian and soldier alike, Germany kept fighting with "
             "incredible determination and bravery. Even as Berlin was being strangled by Soviet armies in "
             "late April 1945, they still fought on until Germany's surrender on May 8th.")


    st.markdown('**Faces of the Wehrmacht: ** ')
    video_file = open('Wehrmacht_Faces.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time = 0)


    st.markdown("""
    ### **The Dead**
    Below are detailed records of the Wehrmacht dead. These records will show when, where, and how many 
    soldiers were killed. Further explanation of the deaths will be provided later.
    
    The first table and plot display general death information from the beginning of the war to the end. 
    Both monthly and cumulative deaths are provided. 
    
    """)

    warMonths = ["Sept-39", "Oct-39", "Nov-39", "Dec-39", "Jan-40", "Feb-40", "Mar-40", "April-40", "May-40",
             "June-40", "July-40", "Aug-40", "Sept-40", "Oct-40", "Nov-40", "Dec-40", "Jan-41", "Feb-41",
             "Mar-41", "April-41", "May-41", "June-41", "July-41", "Aug-41", "Sept-41", "Oct-41", "Nov-41",
             "Dec-41", "Jan-42", "Feb-42", "Mar-42", "April-42", "May-42", "June-42", "July-42", "Aug-42",
             "Sept-42", "Oct-42", "Nov-42", "Dec-42", "Jan-43", "Feb-43", "Mar-43", "April-43", "May-43",
             "June-43", "July-43", "Aug-43", "Sept-43", "Oct-43", "Nov-43", "Dec-43", "Jan-44", "Feb-44",
             "Mar-44", "April-44", "May-44", "June-44", "July-44", "Aug-44", "Sept-44", "Oct-44", "Nov-44",
             "Dec-44", "Jan-45", "Feb-45", "Mar-45", "April-45", "May-45"]
# count = 69

    grossWarDeaths = [15000, 3000, 1000, 0, 2000, 0, 5000, 3000, 21000, 29000, 7000, 4000, 4000,
                  5033, 1000, 2000, 10000, 1000, 4000, 4000, 13000, 29000, 67132, 51066, 53033, 44099,
                  38000, 42198, 53165, 52099, 46132, 24066, 44099, 34033, 46099, 74231, 46033, 30000, 38231,
                  83792, 185376, 74363, 59099, 21066, 31099, 21066, 79231, 66198, 69495, 61330, 77396, 66330,
                  81330, 91495, 112759, 92363, 78495, 182178, 215013, 348960, 151957, 184089, 103561, 159386, 451742,
                  294772, 284442, 281848, 94528]

    grossWarCumm = [15000, 18000, 19000, 19000, 21000, 21000, 26000, 29000, 50000, 79000, 86000,
                90000, 94000, 99033, 100033, 102033, 112033, 113033, 117033, 121033, 134033, 163033,
                230165, 281231, 334264, 378363, 416363, 458561, 511726, 563825, 609957, 634023, 678122,
                712155, 758254, 832485, 878518, 908518, 946749, 1030541, 1215917, 1290280, 1349379, 1370445,
                1401544, 1422610, 1501841, 1568039, 1637534, 1698864, 1776260, 1842590, 1923920, 2015415, 2128174,
                2220537, 2299032, 2481210, 2696223, 3045183, 3197140, 3381229, 3484790, 3644176, 4095918, 4390690,
                4675132, 4956980, 5051508]


    st.markdown('**Monthly and Cumulative Wehrmacht Deaths:  ** ')
    df = st.cache(pd.read_csv)('Deaths_and_Losses.csv')
    st.write(df)

    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
    fig3.add_trace(go.Bar(x=warMonths, y=grossWarDeaths, name="Monthly"), secondary_y=False)
    fig3.add_trace(go.Scatter(x=warMonths, y=grossWarCumm, name="Cumulative"), secondary_y=True)
# Add figure title
    fig3.update_layout(
    title_text="<b>Monthly and Cumulative Wehrmacht Deaths</b>")
# Set x-axis title
    fig3.update_xaxes(title_text="Month")
# Set y-axes titles
    fig3.update_yaxes(title_text="Monthly Deaths", secondary_y=False)
    fig3.update_yaxes(title_text="Cumulative Deaths", secondary_y=True)

    st.plotly_chart(fig3)

    st.markdown(""" #### Wehrmacht Deaths and Losses Breakdown
    To further delve into the deaths and losses suffered by the Wehrmacht, 
    the war will be divided into three sections:
    
    1. **The Early Years: 1939-1941**
        - Invasion of Poland
        - The Phoney War
        - _Fall Gelb:_ Invasion of France and the Low Countries
        - Battle of Britain and build up for Operation Barbarossa 
        - Impact of the Kriegsmarine and Luftwaffe
    2. **The Middle Years: 1942-1944**
        - Invasion of the Soviet Union
        - Rzhev Meatgrinder
        - _Fall Blau:_ Attack on Stalingrad and the Caucases 
        - Failures at Stalingrad
        - Operation Citadel
        - Normandy 
        - Operation Bagration 
        - Ardenness Counteroffensive
        - Impact of the Kriegsmarine and the Luftwaffe 
    3. **The Final Months: 1945**
        - Failure of Ardneness Counteroffensive
        - Vistula-Oder Offensive
        - Battles for Berlin and Halbe Kessel
        - Impact of the Kriegsmarine and the Luftwaffe 
        
        """)


    img = Image.open("Wounded soldier, lost arm.jpg")
    st.image(img, caption = 'A severely wounded Wehrmacht soldier receiving medical attention')

    st.subheader("The Early Years: 1939-1941")

    img1 = Image.open('Deployment_of_Wehrmacht_1939.jpg')
    st.image(img1, caption = 'Deployment of Wehrmacht Before the War')

    st.write("Germany's attack on Poland was sudden and violent. Wehrmacht generals implemented a new "
             "strategy: _Blitzkrieg_. The philosophy behind _Blitzkrieg_ is surprisingly simple. Instead "
             "of having the panzer (tank) and armored units fight alongside the infantry as a support, the "
             "roles were switched. Panzer divisions were formed and they would spearhead the assault while "
             "the infantry would support the armor. Ahead of the panzers, though, the Luftwaffe would be "
             "sent to soften hard targets and intimidate the enemy into submission. These three unified "
             "tactics formed the core principles of _Blitzkrieg_ and would be followed on more than once "
             "throughout the war.")

    st.write("After Poland fell, the Wehrmacht regrouped, retrained, and rested. What follows is a rather "
             "interesting period of the war: The Phoney War or _Sitzkrieg_. This was a period of about eight "
             "months where there was little to no combat on land. The Germans utilize this time to perfect "
             "_Blitzkrieg_ and strategize the invasion of Norway, Denmark, France and the Low Countries. "
             "France, however, did invade and occupy the Saarland briefly. The French would retreat allowing "
             "Germany to continue building its forces up.")

    st.write("In May 1940, after months of careful planning by the High Command, Germany rolled across Belgium "
             "and the Ardennes into France and the Low Countries. Going around the heavily defended Maginot Line, "
             "the Wehrmacht was able to steam across Belgium and Northern France. Fully utilizing Blitzkrieg "
             "strategy, the _Heer_ supported by the _Luftwaffe_, smashed French defenses, seized key bridges "
             "behind the lines, and routed French and British units culminating with the evacuation of 250,000 "
             "men from Dunkirk and the eventual capitulation of France in June 1940, less than six weeks after "
             "the start of the invasion.")

    st.write("")



    st.subheader("The Middle Years: 1942-1944")
    st.markdown('**Fighting on the Eastern Front: ** ')
    video_file = open('Eastern Front.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time = 0)



    st.subheader("Summary of the Deaths")

    img2 = Image.open('German Graves at Stalingrad.jpg')
    st.image(img2, caption = 'German Graves at Stalingrad')

    st.write("From the Atlantic ocean to the River Volga, millions of Germans died fighting for the Third Reich. "
             "Victims of their own propaganda, they fought for a 'United Europe'. Despite this spread, however, "
             "the vast majority of men were sent to the Eastern Front to fight the Soviet Union. The dispropotion "
             "is clearly evident in the table and pie charts. ")

    st.write("The 'Other Theater' category mostly comprises of _Kriegsmarine_ deaths in the Atlantic and deaths "
             "at home defending Germany from Allied air attacks. The deaths in the data below are specified as combat "
             "deaths. As in the men died as a result of combat, either while in action of after and succumbing "
             "to their wounds. Dying in captivity as a POW is another category all together. ")

    st.markdown('**Wehrmacht Combat Deaths by Theater of Engagement**')
    df17 = st.cache(pd.read_csv)('Wehrmacht_Theater.csv')
    st.write(df17)

    st.write("The author of the data notes why 'Final Battles' is its own category. The author notes that as 1944 "
             "turned to 1945, the fronts all started to breakdown. The fronts started to merge together, "
             "difficult to distinguish from one another. Units and individual soldiers started to move west if "
             "it was possible for them to surrender to the more forgiving Western Allies. 'Final Battles' is "
             "defined as the last months of the war, from Jan-May 1945. ")

    st.write("The following data refers to Wehrmacht servicemen died. As is clearly visible, over half of all "
             "soldiers died fighting on the Eastern Front fighting the Soviet Union. From the opening shots "
             "against the Soviet Union in June 1941, to Operation Bagration in July 1944, Wehrmacht soldiers "
             "died. As the war progressed, the Soviet Union was able to amass an army that the Wehrmacht "
             "could only dream of matching in size. ")


    theater1 = ['African', 'Balkans', 'Northern', 'Western', 'Italian', 'Eastern', 'Final Battles', 'Other']
    theaterDeaths = [16066, 103693, 30165, 339957, 150660, 2742909, 1230045, 245561]
    fig6 = px.pie(df17, values=theaterDeaths, names = theater1, title = '<b>Wehrmacht Combat Deaths by Theater<b>')
    st.plotly_chart(fig6)

    st.write("**Eastern Front Deaths Compared to All Other Fronts**")
    df18 = st.cache(pd.read_csv)('Eastern_Front_Deaths.csv')
    st.write(df18)

    st.write("Fighting on all other fronts took a back seat to the Eastern front in terms of importance. Hitler "
             "prioritized the Eastern for men and material at the expense of the others. The largest and most "
             "deadly battles happened out East. Whether it was at Stalingrad, Kursk, or the Rzhev Meatgrinder, "
             "German troops and machines perished at an alarming rate. ")

    st.write("The plot below clearly shows the disparity between the Eastern Front and the rest. It isn't until "
             "later in the war that deaths in all of the other fronts start to approach the same levels as out "
             "East. ")


    eastMonths = ["June-41", "July-41", "Aug-41", "Sept-41", "Oct-41", "Nov-41", "Dec-41", "Jan-42", "Feb-42",
                  "Mar-42", "April-42", "May-42", "June-42", "July-42", "Aug-42", "Sept-42", "Oct-42", "Nov-42",
                  "Dec-42", "Jan-43", "Feb-43", "Mar-43", "April-43", "May-43", "June-43", "July-43", "Aug-43",
                  "Sept-43", "Oct-43", "Nov-43", "Dec-43", "Jan-44", "Feb-44", "Mar-44", "April-44", "May-44",
                  "June-44", "July-44", "Aug-44", "Sept-44", "Oct-44", "Nov-44", "Dec-44"]

    eastDeaths = [25000, 63099, 46066, 51033, 41099, 36000, 40198, 48165, 44099, 44132, 23066, 38099, 29033,
                  38066, 62165, 45033, 25000, 31198, 78759, 180310, 68330, 46066, 16000, 19066, 13066, 71231,
                  59198, 57429, 53264, 67363, 49330, 70330, 64429, 93660, 73264, 48363, 142079, 169881, 277465,
                  70561, 92528, 45363, 85023]
    # count = 43
    otherDeaths = [4000, 4033, 5000, 2000, 3000, 2000, 2000, 5000, 8000, 2000, 1000, 6000,
                   5000, 8033, 12066, 1000, 5000, 7033, 5033, 5066, 6033, 13033, 5066, 12033,
                   8000, 8000, 7000, 12066, 8066, 10033, 17000, 11000, 27066, 19099, 19099, 30132,
                   40099, 45132, 71495, 81396, 91561, 58198, 74363]

    eastCum = [25000, 88099, 134165, 185198, 226297, 262297, 302495, 350660, 394759, 438891, 461957,
               500056, 529089, 567155, 629320, 674353, 699353, 730551, 809310, 989620, 1057950, 1104016,
               1120016, 1139082, 1152148, 1223379, 1282577, 1340006, 1393270, 1460633, 1509963, 1580293,
               1644722, 1738382, 1811646, 1860009, 2002088, 2171969, 2449434, 2519995, 2612523, 2657886,
               2742909]

    otherCum = [4000,   8033,   13033,  15033,  18033,  20033,  22033,  27033,  35033,  37033,
                38033,  44033,  49033,  57066,  69132,  70132,  75132,  82165,  87198,  92264,
                98297,  111330, 116396, 128429, 136429, 144429, 151429, 163495, 171561, 181594,
                198594, 209594, 236660, 255759, 274858, 304990, 345089, 390221, 461716, 543112,
                634673, 692871, 767234]



    fig7 = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
    fig7.add_trace(go.Bar(x=eastMonths, y=eastDeaths, name="Eastern",
                          base=dict(color='midnightblue')), secondary_y=False)
    fig7.add_trace(go.Bar(x=eastMonths, y=otherDeaths, name="Other"), secondary_y=False)
    fig7.add_trace(go.Scatter(x=eastMonths, y=eastCum, name="East Cum."), secondary_y=True)
    fig7.add_trace(go.Scatter(x=eastMonths, y=otherCum, name="Other Cum.",
                              line=dict(color='cyan')), secondary_y=True)
# Add figure title
    fig7.update_layout(title_text="<b>Monthly and Cumulative Deaths on Eastern and All Other Fronts</b>")
# Set x-axis title
    fig7.update_xaxes(title_text="Month")
# Set y-axes titles
    fig7.update_yaxes(title_text="Monthly Deaths", secondary_y=False)
    fig7.update_yaxes(title_text="Cumulative Deaths", secondary_y=True)

    st.plotly_chart(fig7)







if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())




