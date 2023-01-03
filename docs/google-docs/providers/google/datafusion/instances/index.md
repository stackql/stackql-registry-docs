---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - datafusion
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datafusion.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}. |
| `description` | `string` | A description of this instance. |
| `enableRbac` | `boolean` | Option to enable granular role-based access control. |
| `accelerators` | `array` | List of accelerators enabled for this CDF instance. |
| `state` | `string` | Output only. The current state of this Data Fusion instance. |
| `stateMessage` | `string` | Output only. Additional information about the current state of this Data Fusion instance if available. |
| `gcsBucket` | `string` | Output only. Cloud Storage bucket generated by Data Fusion in the customer project. |
| `createTime` | `string` | Output only. The time the instance was created. |
| `labels` | `object` | The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels. |
| `p4ServiceAccount` | `string` | Output only. P4 service account for the customer project. |
| `dataprocServiceAccount` | `string` | User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines. This allows users to have fine-grained access control on Dataproc's accesses to cloud resources. |
| `enableStackdriverLogging` | `boolean` | Option to enable Stackdriver Logging. |
| `eventPublishConfig` | `object` | Confirguration of PubSubEventWriter. |
| `cryptoKeyConfig` | `object` | The crypto key configuration. This field is used by the Customer-managed encryption keys (CMEK) feature. |
| `updateTime` | `string` | Output only. The time the instance was last updated. |
| `privateInstance` | `boolean` | Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet. |
| `serviceEndpoint` | `string` | Output only. Endpoint on which the Data Fusion UI is accessible. |
| `tenantProjectId` | `string` | Output only. The name of the tenant project. |
| `options` | `object` | Map of additional options used to configure the behavior of Data Fusion instance. |
| `version` | `string` | Current version of the Data Fusion. Only specifiable in Update. |
| `serviceAccount` | `string` | Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID. |
| `displayName` | `string` | Display name for an instance. |
| `enableStackdriverMonitoring` | `boolean` | Option to enable Stackdriver Monitoring. |
| `apiEndpoint` | `string` | Output only. Endpoint on which the REST APIs is accessible. |
| `networkConfig` | `object` | Network configuration for a Data Fusion instance. These configurations are used for peering with the customer network. Configurations are optional when a public Data Fusion instance is to be created. However, providing these configurations allows several benefits, such as reduced network latency while accessing the customer resources from managed Data Fusion instance nodes, as well as access to the customer on-prem resources. |
| `type` | `string` | Required. Instance type. |
| `disabledReason` | `array` | Output only. If the instance state is DISABLED, the reason for disabling the instance. |
| `zone` | `string` | Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field. |
| `availableVersion` | `array` | Available versions that the instance can be upgraded to using UpdateInstanceRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Data Fusion instance. |
| `projects_locations_instances_list` | `SELECT` | `locationsId, projectsId` | Lists Data Fusion instances in the specified project and location. |
| `projects_locations_instances_create` | `INSERT` | `locationsId, projectsId` | Creates a new Data Fusion instance in the specified project and location. |
| `projects_locations_instances_delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Date Fusion instance. |
| `projects_locations_instances_patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates a single Data Fusion instance. |
| `projects_locations_instances_restart` | `EXEC` | `instancesId, locationsId, projectsId` | Restart a single Data Fusion instance. At the end of an operation instance is fully restarted. |