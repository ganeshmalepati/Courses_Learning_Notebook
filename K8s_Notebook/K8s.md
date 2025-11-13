K8s 

---

&nbsp;



Kubernetes (K8s) is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.



✅ Why Use Kubernetes:



* Scalability: Automatically scale apps up/down based on demand.
* High Availability: Ensures apps stay running even if some containers fail.
* Self-Healing: Automatically replaces failed containers.
* Rolling Updates: Deploy new versions without downtime.
* Resource Optimization: Efficient use of hardware resources.





✅ Real-Time Use Case:

E-commerce App: During festive sales, traffic spikes. Kubernetes can auto-scale the backend services to handle the load and scale down after the sale ends.





✅ Key Components:

🧱 Node:



A physical or virtual machine where containers run.

Two types: Master Node (Control Plane) and Worker Node.



🧱 Pod:



The smallest deployable unit in Kubernetes.

A Pod can contain one or more containers that share storage/network.



🧱 Container:



A lightweight, portable unit that runs your application.







Container Orchestration:- A container orchestration technology used to orchestrate that manages and deploys thousands of containers in a cluster.



K8s Architecture

----------------



A Cluster is a set of nodes grouped together even one node fails you can access application with the other node . 



Who can manage the cluster :- Master it's responsible for checking the node and managing of node in the cluster.



Components

-----------

API Server:- CLI talk to k8s API services 



etcd :- key-value store ->To store all the data used to manage the cluster. multiple node and multiple master in the cluster 

--> Stores all the info and nodes in the distributed manner.



Kubelet --> Agent to perform and check the containers are running as expect



Container Runtime--> Used to run containers 



Controller --> The main brain behind the orchestration of the cluster k8s.



🧱 Control Plane:



Manages the cluster. Key components:



* API Server: Entry point for all commands (kubectl).
* Scheduler: Assigns Pods to Nodes.
* Controller Manager: Maintains desired state (e.g., restarts failed Pods).
* etcd: Stores cluster state/configuration.



✅ Real-Time Use Case:

Microservices Architecture: Each microservice (e.g., user service, payment service) runs in its own Pod. Kubernetes ensures they are distributed across nodes and scaled independently.





Commands and Info

-----------------





* kubectl :- Kubernetes command line tool



* kubectl run minikube :- Which is used to deploy an application



* kubectl cluster info :- is used to get the info about the cluster



* kubectl get nodes :- is used to get the nodes info from cluster







Setting Up Mini-Kube or Kubernetes

----------------------------------









POD

----











How to deploy the pods and check the pod status 























------------------------------------------------------------------------------------------------------------------------------------------------------------

ISSUES FACING WHILE SETTING UP THE KUBECTL TO CLI

=================================================



The repeated curl error means the URL is not being interpreted correctly, likely due to WSL quirks or DNS issues. Let’s fix this and give you a complete WSL Kubernetes setup guide that works reliably.



✅ Why This Happens



WSL sometimes misinterprets ${VERSION} if the variable is empty (due to network redirect or DNS failure).

DNS resolution issues in WSL can cause curl to fail.

Using quotes incorrectly or copying from HTML can break the command.





-> Step 1: Fix DNS in WSL

&nbsp;	Edit /etc/resolv.conf:

&nbsp;	

&nbsp;	"sudo nano /etc/resolv.conf"





Add:



&nbsp;	"nameserver 8.8.8.8

&nbsp;	 nameserver 1.1.1.1"





-> Step 2: Install Docker

&nbsp;	

&nbsp;	sudo apt-get update \&\& sudo apt-get install -y docker.io

&nbsp;	sudo systemctl enable docker

&nbsp;	sudo systemctl start docker

&nbsp;	docker --version





-> Step 3: Install kubectl (Reliable Method)



&nbsp;	Instead of using variable substitution, download directly:



&nbsp;	

&nbsp;	curl -LO https://dl.k8s.io/release/v1.30.0/bin/linux/amd64/kubectl

&nbsp;	chmod +x kubectl

&nbsp;	sudo mv kubectl /usr/local/bin/

&nbsp;	kubectl version --client





-> Step 4: Install Minikube



&nbsp;	curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

&nbsp;	sudo install minikube-linux-amd64 /usr/local/bin/minikube

&nbsp;	minikube version







If you get some error like below mentioned:- 

==========================================



"The error you’re seeing is Docker permission issue. Minikube cannot access the Docker socket because your user isn’t in the docker group yet.

Here’s how to fix it and complete your WSL Kubernetes setup:"



✅ Fix Docker Permissions:



&nbsp;	" sudo usermod -aG docker $USER "



Then apply the new group without restarting:



&nbsp;	" newgrp docker"



Now start Minikube again:



&nbsp;	"minikube start --driver=docker"



CHECK NOW : 

&nbsp;	

&nbsp;	minikube status

&nbsp;	kubectl cluster-info

&nbsp;	kubectl get nodes







✅ Why This Happens



By default, only root can access /var/run/docker.sock.

Adding your user to the docker group gives permission.



------------------------------------------------------------------------------------------------------------------------------------------------------------





Info about the load balance

-> Initially there is one pod with some users when the users increases we need to deploy the more pods. so, these can be done by load balancer when the 

&nbsp;  users increased to access app then the load balancer deploys more pods.                          

-> Real-world scenario, At the time of Big-Billon-Days the active users for amazon and flipkart will be huge and there are n number of users can access so 

&nbsp;  they can deploy more pods and increases the count of pods for access this can be done using the load balancer once the sale is ended the users decreases 

&nbsp;  and the pods will scale out automatically using load balancers.







Difference b/w Docker Deployment and K8s Deployment

---------------------------------------------------



The result looks the same because both Docker and Kubernetes ultimately run your containerized app, but they solve different problems. Here’s the key difference:



✅ Docker



Purpose: Builds and runs containers on a single machine.

Scope: Local development or small-scale deployment.

What you did: Ran docker run -p 5000:5000 flask-k8s-app → This started one container on your machine.

Limitations:



No built-in scaling.

No self-healing (if the container crashes, it stays down).

No orchestration across multiple machines.





✅ Kubernetes



Purpose: Orchestrates containers across clusters of machines.

Scope: Production-grade deployments.

What you did: Created a Deployment with replicas and exposed it via a Service.

Advantages:



Scaling: Easily increase replicas (kubectl scale).

Self-Healing: If a Pod fails, Kubernetes restarts it automatically.

Load Balancing: Distributes traffic across Pods.

Rolling Updates: Deploy new versions without downtime.

Cluster Management: Works across multiple nodes, not just one machine.





✅ Why Same Result?



Both run the same container image, so the app looks identical.

The difference is in management, scalability, and resilience—which matters in real-world production.







K8s POD Creation \& CLI Commands

-------------------------------

After creating yaml file for kubernetes to run pods



-> kubectl apply/create -f file\_name.yaml



-> kubectl get deployments



-> kubectl get pods



-> kubectl get services



-> kubectl expose deployment <pod\_name> --type=NodePort --port=80



-> kubectl get svc



-> kubectl get pods -o wide



-> kubectl describe pods <pod\_name>



-> kubectl describe svc <pod\_name>



-> kubectl describe deployments <pod\_name>



-> kubectl scale deployment <pod\_name> --replicas=3



-> kubectl delete deployment <deployment\_name>



-> kubectl delete pod <pod\_name>



-> kubectl delete service <svc\_name>



-> kubetctl autoscale deployment <pod\_name> --cpu-precent=50 --min=2 --max=10



-> kubectl get hpa



-> kubectl delete all --all















