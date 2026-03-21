Jayden Berard

# NP-Hackathon-Spring-2026-Weed-Detection-System

### What global issue does your project attempt to address?
This project attempts to solve and help with optimizing weed removal in crops and farming. The benefit of this allows for a reduce in resource consumption and to find and focus more on high priority which is especially important in communites that dont have access to many options for removal. This project also attempts to be offered as a template so in the future it can be used to be deployed on low power devices such as phones which may not be able to handle alot processing or a custom made device to run this program. Agriculture is a very important topic to know and understand because it is linked to the issue of hunger as without food many communties will starve which is a fate no human being should ever face in there lives.This project was made because of the many crisis happening in many countries such as Haiti which is where my father is from this creation is more of a prototype for a much greater system that would detect many different kinds of weeds and even detect crops so they can be differentiated . So this project serves as a way to help with that goal and maybe in the near future will this program be more advanced and tinkered to be used by even just a person who has nothing but a broken phone so that they can optimize their farming so they can have a better harvest even among the chaos.

### What does your project do to address this issue?
As of now this project uses a Machine Learning Model that can process either images, video, or recording and detect any weeds in the vicinity which unfortauntely only detects one type of weed. It then will display the number of weeds in the area it is detecting ranging from a batch to only one and then you can save the number of weeds detected mutiple types allowing for a graph to be displayed with many different areas and there corresponding weed amout. This can be helpful as know which area requires more work can allow for a much faster removel which is very important for a place that may be in total chaos. Even if it is just a few extra mins saved it can be the differance between crops being slowed or not. 

### How did you build your project?
This project was made with many different tools mainly focusing around python. Tools include Label Studio, Google Colab, YOLO, Jupyter, and many python packages. First I accumulated a dataset made by me using pictures of English Ivy that has been sitting in my backyard for quite some time. The Reason for this was more of experimenting if I could make a decent dataset that could be used for "training" (really fine tuning) a ML model. After retrieving all the pictures they were all labeled in Label Studio and exported to be trained. The data was then used in a public Google Colab YOLO training template to not only train but to also understand the process and the methods requried for such a procedure. After some experimenting YOLOv11 was the model that would be fine tuned into the custom model received. After getting the model it was put into a Jupyter Notebook to test the parameters on images, videos, and even on the webcam where it did a decent job at detecting.

### What challenges did you face?
Many challenges were faced making this project which would explaing its very barebones nature. I did not having any prior knowledge or skill when working on this project but really wanteed to learn the process of atleast developing a ML model on a framework. With the combination of both school, work and getting sidetracked many features that were considered are now sidelined. What I realize now and want to do better in the future is to work with others to not only learn much better but to also be able to build more a much more bigger verison of a project as with many others we can all take a workload and if situation come up we still have multiple people to atleast finish the prototype. What I also realize that maybe 40 images may sllighty (most definitely) not be enough for training a model.

### What’s next for your project?
What I dream of for this project if I ever get the free time is to tweak it more till it is accurate enough to full detect many different types of weeds that can heavily effect crop growth and to either have this program be able to run on a mobile device for much more accessibility and more features to give a much more incentive to use.

### If you used any AI tools, where and how did you use them?
The only use that AI brought was the research aspect of finding a problem to solve from the AI overview by gemini to get an idea

# Tool List
<div>
  <img  width="690" height="362" alt="LabelStudioLogo" src="https://github.com/user-attachments/assets/ced7ea98-6548-4cb5-bcfb-df5bda8b1842" />
  <img  width="690" height="362" alt="GoogleColabLogo" src="https://github.com/user-attachments/assets/c8a88031-2e78-4724-bbf8-d170fb3b089e" />
  <img align="right" width="690" height="362" alt="JupyterLogo" src="https://github.com/user-attachments/assets/acfde116-d305-49e5-adcc-2b98e94df7a4" />
  <img  align="right" width="690" height="362" alt="YoloLogo" src="https://github.com/user-attachments/assets/a0ddd8b4-456e-44c4-86f8-c00442c57d2b" />
</div>
