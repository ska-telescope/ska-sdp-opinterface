Connecting to the Operator interface
====================================

The Operator interface is deployed as a service with the name ``sdp-opinterface`` in a
`Kubernetes deployment <https://developer.skao.int/projects/ska-sdp-integration/en/latest/running/standalone.html>`_ of the SDP system.

For example::

  $ helm install test ska/ska-sdp
  $ kubectl get service sdp-opinterface

  NAME              TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
  sdp-opinterface   NodePort   10.107.71.94   <none>        8000:30422/TCP   5m16s

This example shows the Operator Interface to be available on port 8000 `within the cluster` and
on a `system-assigned port` (30422 in this example - but this will vary) on the `public interface` of the node running the
POD implementing the service.

To use it, it is necessary to connect to the service using a web browser.

.. image:: images/db.png
   :width: 400

Some of the ways to do this are described.

Using minikube::

  On a minikube deployment simply type

  $ minikube service sdp-opinterface

  to connect to the service in the default web browser.

  Alternatively the public IP address of the minikube node is available using the command

  $ minikube ip

  and the service endpoint address will be http://<minikube ip address>:system assigned port> -
  For example http://192.168.49.2:30422




On a cluster started by other means - `kubeadm` for instance::

   $ kubectl get pods --selector="component=sdp-opinterface"
   sdp-opinterface-0   1/1     Running   0          76m   172.17.18.169   alaska-kube-md-0-c2d2f95f-wpj8j
   and then
   $ kubectl get node alaska-kube-md-0-c2d2f95f-wpj8j -o wide
   alaska-kube-md-0-c2d2f95f-wpj8j   Ready    <none>   137d   v1.22.1   192.168.3.63   ...

   where the URL to use would, in this case, be http://192.168.3.63:30422 (assuming the service was on
   the same external port)

