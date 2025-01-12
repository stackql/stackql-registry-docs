---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - clusters
  - compute
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>clusters</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="autotermination_minutes" /> | `integer` |
| <CopyableCode code="aws_attributes" /> | `object` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="cluster_name" /> | `string` |
| <CopyableCode code="cluster_source" /> | `string` |
| <CopyableCode code="creator_user_name" /> | `string` |
| <CopyableCode code="default_tags" /> | `object` |
| <CopyableCode code="disk_spec" /> | `object` |
| <CopyableCode code="driver_instance_source" /> | `object` |
| <CopyableCode code="driver_node_type_id" /> | `string` |
| <CopyableCode code="enable_elastic_disk" /> | `boolean` |
| <CopyableCode code="enable_local_disk_encryption" /> | `boolean` |
| <CopyableCode code="init_scripts_safe_mode" /> | `boolean` |
| <CopyableCode code="instance_source" /> | `object` |
| <CopyableCode code="last_state_loss_time" /> | `integer` |
| <CopyableCode code="node_type_id" /> | `string` |
| <CopyableCode code="num_workers" /> | `integer` |
| <CopyableCode code="spark_context_id" /> | `integer` |
| <CopyableCode code="spark_version" /> | `string` |
| <CopyableCode code="start_time" /> | `integer` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="state_message" /> | `string` |
| <CopyableCode code="terminated_time" /> | `integer` |
| <CopyableCode code="termination_reason" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cluster_id, deployment_name" /> | Retrieves the information for a cluster given its identifier. Clusters can be described while they are running, or up to 60 days after they are terminated. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Return information about all pinned and active clusters, and all clusters terminated within the last 30 days. Clusters terminated prior to this period are not included. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new Spark cluster. This method will acquire new instances from the cloud provider if necessary. This method is asynchronous; the returned |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Terminates the Spark cluster with the specified ID. The cluster is removed asynchronously. Once the termination has completed, the cluster will be in a |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the configuration of a cluster to match the partial set of attributes and size. Denote which fields to update using the |
| <CopyableCode code="edit" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Updates the configuration of a cluster to match the provided attributes and size. A cluster can be updated if it is in a |
| <CopyableCode code="changeowner" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Change the owner of the cluster. You must be an admin and the cluster must be terminated to perform this operation. The service principal application ID can be supplied as an argument to |
| <CopyableCode code="permanentdelete" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Permanently deletes a Spark cluster. This cluster is terminated and resources are asynchronously removed. |
| <CopyableCode code="pin" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Pinning a cluster ensures that the cluster will always be returned by the ListClusters API. Pinning a cluster that is already pinned will have no effect. This API can only be called by workspace admins. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Resizes a cluster to have a desired number of workers. This will fail unless the cluster is in a |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Restarts a Spark cluster with the supplied ID. If the cluster is not currently in a |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Starts a terminated Spark cluster with the supplied ID. This works similar to |
| <CopyableCode code="unpin" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Unpinning a cluster will allow the cluster to eventually be removed from the ListClusters API. Unpinning a cluster that is not pinned will have no effect. This API can only be called by workspace admins. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'clusters (list)', value: 'list' },
        { label: 'clusters (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
autotermination_minutes,
aws_attributes,
cluster_id,
cluster_name,
cluster_source,
creator_user_name,
default_tags,
disk_spec,
driver_instance_source,
driver_node_type_id,
enable_elastic_disk,
enable_local_disk_encryption,
init_scripts_safe_mode,
instance_source,
last_state_loss_time,
node_type_id,
num_workers,
spark_context_id,
spark_version,
start_time,
state,
state_message,
terminated_time,
termination_reason
FROM databricks_workspace.compute.clusters
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
autotermination_minutes,
aws_attributes,
cluster_id,
cluster_name,
cluster_source,
creator_user_name,
default_tags,
disk_spec,
driver_instance_source,
driver_node_type_id,
enable_elastic_disk,
enable_local_disk_encryption,
init_scripts_safe_mode,
instance_source,
last_state_loss_time,
node_type_id,
num_workers,
spark_context_id,
spark_version,
start_time,
state,
state_message,
terminated_time,
termination_reason
FROM databricks_workspace.compute.clusters
WHERE cluster_id = '{{ cluster_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

<Tabs
    defaultValue="all"
    values={[
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },    
    ]}
>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.clusters (
deployment_name,
data__kind,
data__cluster_name,
data__spark_version,
data__use_ml_runtime,
data__is_single_node,
data__node_type_id,
data__autoscale,
data__num_workers,
data__data_security_mode,
data__runtime_engine,
data__enable_elastic_disk,
data__aws_attributes,
data__cluster_log_conf,
data__init_scripts,
data__spark_conf,
data__spark_env_vars,
data__driver_node_type_id,
data__ssh_public_keys,
data__custom_tags,
data__single_user_name,
data__autotermination_minutes,
data__enable_local_disk_encryption,
data__policy_id,
data__apply_policy_default_values,
data__instance_pool_id,
data__driver_instance_pool_id,
data__docker_image,
data__workload_type,
data__clone_from
)
SELECT 
'{{ deployment_name }}',
'{{ kind }}',
'{{ cluster_name }}',
'{{ spark_version }}',
 {{ use_ml_runtime }},
 {{ is_single_node }},
'{{ node_type_id }}',
'{{ autoscale }}',
 {{ num_workers }},
'{{ data_security_mode }}',
'{{ runtime_engine }}',
 {{ enable_elastic_disk }},
'{{ aws_attributes }}',
'{{ cluster_log_conf }}',
'{{ init_scripts }}',
'{{ spark_conf }}',
'{{ spark_env_vars }}',
'{{ driver_node_type_id }}',
'{{ ssh_public_keys }}',
'{{ custom_tags }}',
'{{ single_user_name }}',
 {{ autotermination_minutes }},
 {{ enable_local_disk_encryption }},
'{{ policy_id }}',
 {{ apply_policy_default_values }},
'{{ instance_pool_id }}',
'{{ driver_instance_pool_id }}',
'{{ docker_image }}',
'{{ workload_type }}',
'{{ clone_from }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: databricks_cluster_resource
  props:
  - name: kind 
    description: The kind of compute described by this compute specification (required)
    value: "CLASSIC_PREVIEW"
  - name: cluster_name
    description: Cluster name requested by the user, does not need to be unique. If not specified at creation, the cluster name will be an empty string.
    value: single-node-with-kind-cluster
  - name: spark_version
    description: The Spark version of the cluster, e.g. 3.3.x-scala2.11 (required)
    value: 14.3.x-scala2.12
  - name: use_ml_runtime
    description: Controls ML runtime usage, dependent on kind field and node_type_id (GPU)  
    value: false
  - name: is_single_node
    description: When true, configures single node related tags, conf, and workers
    value: true
  - name: node_type_id
    description: The node type for provisioning cluster resources (e.g. memory/compute optimized)
    value: i3.xlarge
  - name: autoscale
    description: Parameters for automatic cluster scaling based on load
    value:
      min_workers: 2  # Minimum number of workers cluster can scale down to (integer)
      max_workers: 8  # Maximum number of workers cluster can scale up to (integer)
  - name: num_workers
    description: Number of worker nodes in cluster, total nodes is num_workers + 1 (driver)
    value: 0
  - name: data_security_mode
    description: Data security mode determines data governance model for cluster access
    value: "SINGLE_USER"  # Options listed below:
    # DATA_SECURITY_MODE_AUTO: Databricks chooses based on compute config
    # DATA_SECURITY_MODE_STANDARD: Alias for USER_ISOLATION
    # DATA_SECURITY_MODE_DEDICATED: Alias for SINGLE_USER  
    # NONE: No security isolation, data governance unavailable
    # SINGLE_USER: Secure single-user cluster with full features
    # USER_ISOLATION: Secure multi-user cluster with some feature limits
    # Legacy modes (deprecated in DBR 15.0+):
    # LEGACY_TABLE_ACL: For legacy Table ACL migration
    # LEGACY_PASSTHROUGH: For legacy high concurrency clusters
    # LEGACY_SINGLE_USER: For legacy standard clusters
    # LEGACY_SINGLE_USER_STANDARD: No UC/passthrough mode
  - name: runtime_engine
    description: Determines cluster's runtime engine - standard or Photon
    value: "STANDARD"  # Options - STANDARD, PHOTON
  - name: enable_elastic_disk
    description: Enables autoscaling of local storage for Spark
    value: true
  - name: aws_attributes
    description: AWS-specific attributes for cluster configuration
    value:
      first_on_demand: 1       # Number of on-demand instances before spot (integer)
      availability: SPOT_WITH_FALLBACK  # Instance availability type - SPOT, ON_DEMAND, SPOT_WITH_FALLBACK  
      zone_id: auto            # AWS availability zone for cluster (e.g., us-west-2a)
      spot_bid_price_percent: 100  # Spot instance bid price as % of on-demand price (integer, max 10000)
      ebs_volume_count: 0      # Number of EBS volumes per instance (integer, 0-10)
      ebs_volume_size: 100     # Size of each EBS volume in GB (integer) 
      ebs_volume_type: GENERAL_PURPOSE_SSD  # EBS volume type (string)
      instance_profile_arn: "" # Optional IAM instance profile ARN for cluster nodes
      ebs_volume_iops: null    # Optional IOPS for gp3 volumes
      ebs_volume_throughput: null # Optional throughput for gp3 volumes
  - name: cluster_log_conf
    description: Configuration for spark log delivery to storage
    value:
      dbfs:  # Only one destination type allowed
        destination: "dbfs:/cluster-logs"  # DBFS path for logs
      # Alternative S3 configuration:
      # s3:
      #   destination: "s3://my-bucket/logs"
      #   region: "us-west-2"  # or endpoint URL
      #   enable_encryption: false
      #   encryption_type: "sse-s3"  # or sse-kms
      #   kms_key: ""  # KMS key for sse-kms
      #   canned_acl: "bucket-owner-full-control"
  - name: init_scripts
    description: Scripts to run during cluster startup
    value:
      - workspace:  # Workspace file location
          destination: "/Users/user@example.com/init.sh"
      # Alternative locations:
      # - dbfs:
      #     destination: "dbfs:/path/init.sh"
      # - s3:
      #     destination: "s3://bucket/init.sh"
      #     region: "us-west-2"
      # - volumes:
      #     destination: "/Volumes/init.sh"
  - name: spark_conf
    description: Spark configuration key-value pairs including JVM options
    value:
      "spark.speculation": true
      "spark.streaming.ui.retainedBatches": 5
  - name: spark_env_vars
    description: Environment variables set on all cluster nodes
    value:
      "SPARK_WORKER_MEMORY": "28000m"
      "SPARK_LOCAL_DIRS": "/local_disk0"
  - name: driver_node_type_id 
    description: Optional separate node type for Spark driver (defaults to node_type_id)
    value: i3.xlarge
  - name: ssh_public_keys
    description: SSH public keys added to each Spark node (max 10)
    value: []
  - name: custom_tags
    description: Additional tags for cluster resources (max 45 tags)
    value:
      Provisioner: stackql
      StackName: "{{ stack_name }}"
      StackEnv: "{{ stack_env }}" 
  - name: single_user_name
    description: Username if data_security_mode is SINGLE_USER
    value: "user@example.com"
  - name: autotermination_minutes
    description: Minutes of inactivity before cluster termination (10-10000, 0 to disable)
    value: 120
  - name: enable_local_disk_encryption
    description: Enable LUKS encryption on cluster VM local disks
    value: true
  - name: policy_id
    description: ID of cluster policy to apply
    value: ""
  - name: apply_policy_default_values
    description: Use policy defaults (true) or only fixed values (false) for omitted fields
    value: false
  - name: instance_pool_id
    description: ID of instance pool for cluster nodes
    value: ""
  - name: driver_instance_pool_id
    description: Optional separate instance pool ID for driver node
    value: ""
  - name: docker_image
    description: Custom docker image configuration
    value:
      url: "repo/image:tag"  # Docker image URL
      basic_auth:
        username: ""  # Registry authentication
        password: ""
  - name: workload_type
    description: Defines what type of clients can use the cluster
    value:
      clients:
        notebooks: true  # Allow notebook workloads
        jobs: true      # Allow job workloads
  - name: clone_from        
    description: When specified, this clones libraries from a source cluster during the creation of a new cluster.
    value:
      source_cluster_id: "1202-211320-brick1" # The cluster that is being cloned (required).
```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.compute.clusters
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>clusters</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.compute.clusters
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.clusters
WHERE deployment_name = '{{ deployment_name }}';
```
