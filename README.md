# Kubernetes Learning (Basics → Certified)

This repository is a hands-on Kubernetes learning workspace: short notes plus practical YAML manifests you can apply to a cluster while learning core concepts (pods, deployments, services, ingress, storage, autoscaling, security, scheduling, and more).

## Who this is for

- You’re learning Kubernetes and want small, focused examples.
- You want a personal “lab notebook” style repo you can revisit later.

## Prerequisites

- A Kubernetes cluster: `kind`, `minikube`, Docker Desktop Kubernetes, or a real cluster
- `kubectl` configured to talk to that cluster
- Optional: `helm` (only if you try ingress controller setups that use Helm)

## How to use this repo

1. Pick a topic folder (for example `pods/` or `services/`).
2. Read the YAMLs and apply them to a non-production namespace.
3. Inspect resources with `kubectl get/describe/logs`, then delete what you created.

Typical workflow:

```bash
# (optional) create a sandbox namespace
kubectl create ns learning

# apply an example
kubectl -n learning apply -f <file-or-folder>

# observe
kubectl -n learning get all

# cleanup
kubectl -n learning delete -f <file-or-folder>
```

## Repository map (topics)

Most folders are named after the concept they demonstrate:

- Core building blocks: `basics/`, `pods/`, `replicas/`, `deployments/`
- Networking: `services/`, `networking/`, `ingress_controller/`, `ingress_full_steps_example/`, `tls/`
- Configuration: `config_maps/`, `secrets/`, `environment_variables/`
- Workloads: `jobs/`, `cron_jobs/`, `daemon_sets/`, `stateful_sets_and_headless_service/`, `multi_container_pods/`, `static_pods/`
- Scheduling: `node_selectors/`, `node_affinity/`, `taints_toleration/`, `priority_classes/`, `custom_schedulers/`
- Resources & policy: `resources_requirements/`, `limit_ranges/`, `resource_quotas/`, `Horizontal_pod_AutoScaling/`, `Vertical_Pod_AutoScaling/`
- Storage: `persistent_volumes/`, `storage_class/`
- Security & access: `service_accounts/`, `security/`, `adminssion_controllers/`, `user_acounts/`
- Rollouts: `rollouts_and_versioning/`
- Docker practice: `Docker_with_example/`, `Docker_practice_todo_app/`, `basic_docker_entrypoint_and_cmd_and_k8s/`

Note: some folder names contain typos but are kept as-is to avoid breaking paths.

## Notes / conventions

- Treat all manifests as learning examples; review and adapt before using anywhere serious.
- Prefer applying to a dedicated namespace (e.g. `learning`) and cleaning up afterwards.

## Contributing

If you find a mistake or want to add an example, feel free to open a PR.
