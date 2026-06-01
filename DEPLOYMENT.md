# Deployment Guide: Harness Kernel

This guide outlines how to deploy the Harness Kernel components and generate the required gRPC language bindings using `protoc`.

## 1. Prerequisites
Ensure you have the following installed:
- `protoc` (Protocol Buffer Compiler)
- `grpcio-tools` (Python gRPC support)

## 2. Generating Protocol Bindings
To generate the necessary code from `harness.proto`, run the following command from the project root:

```bash
# Generate Python bindings
python3 -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/harness.proto
```

This will create:
- `harness_pb2.py`: Data structures.
- `harness_pb2_grpc.py`: Service stubs for the Harness Protocol.

## 3. Service Deployment
The Harness Kernel is designed to run as distributed microservices:

1.  **Governance Service:**
    - Deploy `services/governance/engine.py` as a gRPC server.
    - Mount `services/governance/policy.yaml` as a config map or volume.
2.  **AFR Service:**
    - Deploy the Flight Recorder as an event-streaming service.
3.  **Runtime:**
    - Point the `HarnessRuntime` to the internal network addresses of the Governance and AFR services.

## 4. Configuration
Ensure your `YAML` policies are updated to reflect your environment's compliance requirements before deployment.

---
*For questions regarding deployment in Kubernetes, see ARCHITECTURE.md.*
