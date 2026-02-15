# Kubernetes Learning (Basics → Certified)

This repository is a hands-on Kubernetes learning workspace: short notes plus practical YAML manifests you can apply to a cluster while learning core concepts (pods, deployments, services, ingress, storage, autoscaling, security, scheduling, and more).

## Who this is for

- You’re learning Kubernetes and want small, focused examples.
- You want a personal “lab notebook” style repo you can revisit later.

## Prerequisites

- Basic Understanding of Docker as well
- A Kubernetes cluster: `kind`, `minikube`, Docker Desktop Kubernetes, or a real cluster
- `kubectl` configured to talk to that cluster
- Optional: `helm` (only if you try ingress controller setups that use Helm)

## Docker Architecture : 
![Docker Architecture](Docker/docker_architecture.png)


## Kubernetes Architecture : 
![Kubernetes Architecture](Kubernetes/k8s_architecture.png)

## Clone this repo

```bash
git clone git@github.com:ARPITJAINECE/kubernetes_learning.git
cd kubernetes_learning
```

If you don’t have SSH set up for GitHub, use HTTPS:

```bash
git clone https://github.com/ARPITJAINECE/kubernetes_learning.git
cd kubernetes_learning
```

## How to use this repo

### Start here: Cluster access (authn/authz) + certificates

If you’re new to Kubernetes access, start with `Kubernetes/00_access_auth_certificates/` first:

- `Kubernetes/00_access_auth_certificates/vanilla_cluster/`: client certificate (CSR) flow + kubeconfig + RBAC
- `Kubernetes/00_access_auth_certificates/eks/`: EKS authentication (IAM) + authorization (RBAC) flow

1. Pick a topic folder (for example `Kubernetes/pods/` or `Kubernetes/services/`).
2. Read the YAMLs and apply them to a non-production namespace.
3. Inspect resources with `kubectl get/describe/logs`, then delete what you created.

Learning workflow (create → observe → cleanup):

```bash
# 1) (recommended) create a sandbox namespace for all experiments
kubectl create namespace learning

# 2) Create objects from an example (pick a YAML file or a whole folder)
kubectl -n learning apply -f <path-to-yaml>
# or:
kubectl -n learning apply -f <path-to-folder>

# 3) Observe what you created
kubectl -n learning get all
kubectl -n learning describe <kind>/<name>
kubectl -n learning get events --sort-by=.metadata.creationTimestamp

# 4) Debug (common commands)
kubectl -n learning logs <pod-name> --all-containers --tail=200
kubectl -n learning exec -it <pod-name> -- sh

# 5) Cleanup (delete what you applied)
kubectl -n learning delete -f <path-to-yaml-or-folder>
```

Tips:

- Start small: apply one YAML at a time, verify it works, then move to the next.
- Keep one namespace per learning session (e.g. `learning`) so cleanup is easy.
- Prefer `kubectl apply` for iterating and `kubectl delete` to reset.

## Repository map (topics)

Most folders are named after the concept they demonstrate:

- Start here (access): `Kubernetes/00_access_auth_certificates/`
- Core building blocks: `Kubernetes/basics/`, `Kubernetes/pods/`, `Kubernetes/replicas/`, `Kubernetes/deployments/`
- Networking: `Kubernetes/services/`, `Kubernetes/networking/`, `Kubernetes/ingress_controller/`, `Kubernetes/ingress_full_steps_example/`, `Kubernetes/tls/`
- Configuration: `Kubernetes/config_maps/`, `Kubernetes/secrets/`, `Kubernetes/environment_variables/`
- Workloads: `Kubernetes/jobs/`, `Kubernetes/cron_jobs/`, `Kubernetes/daemon_sets/`, `Kubernetes/stateful_sets_and_headless_service/`, `Kubernetes/multi_container_pods/`, `Kubernetes/static_pods/`
- Scheduling: `Kubernetes/node_selectors/`, `Kubernetes/node_affinity/`, `Kubernetes/taints_toleration/`, `Kubernetes/priority_classes/`, `Kubernetes/custom_schedulers/`
- Resources & policy: `Kubernetes/resources_requirements/`, `Kubernetes/limit_ranges/`, `Kubernetes/resource_quotas/`, `Kubernetes/Horizontal_pod_AutoScaling/`, `Kubernetes/Vertical_Pod_AutoScaling/`
- Storage: `Kubernetes/persistent_volumes/`, `Kubernetes/storage_class/`
- Security & access: `Kubernetes/service_accounts/`, `Kubernetes/security/`, `Kubernetes/adminssion_controllers/`, `Kubernetes/user_acounts/`
- Rollouts: `Kubernetes/rollouts_and_versioning/`
- Docker practice: `Docker/Docker_with_example/`, `Docker/Docker_practice_todo_app/`, `Docker/basic_docker_entrypoint_and_cmd_and_k8s/`

Note: some folder names contain typos but are kept as-is to avoid breaking paths.

## Notes / conventions

- Treat all manifests as learning examples; review and adapt before using anywhere serious.
- Prefer applying to a dedicated namespace (e.g. `learning`) and cleaning up afterwards.

## Contributing

If you find a mistake or want to add an example, feel free to open a PR.
