---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
  - run
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique name of this Revision. |
| `serviceAccount` | `string` | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. |
| `scaling` | `object` | Settings for revision-level scaling settings. |
| `encryptionKey` | `string` | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
| `encryptionKeyRevocationAction` | `string` | The action to take if the encryption key is revoked. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `createTime` | `string` | Output only. The creation time. |
| `logUri` | `string` | Output only. The Google Console URI to obtain logs for the Revision. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Service.reconciling` for additional information on reconciliation process in Cloud Run. |
| `timeout` | `string` | Max allowed time for an instance to respond to a request. |
| `maxInstanceRequestConcurrency` | `integer` | Sets the maximum number of requests that each serving instance can receive. |
| `executionEnvironment` | `string` | The execution environment being used to host this Revision. |
| `vpcAccess` | `object` | VPC Access settings. For more information on creating a VPC Connector, visit https://cloud.google.com/vpc/docs/configure-serverless-vpc-access For information on how to configure Cloud Run with an existing VPC Connector, visit https://cloud.google.com/run/docs/configuring/connecting-vpc |
| `containers` | `array` | Holds the single container that defines the unit of execution for this Revision. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `volumes` | `array` | A list of Volumes to make available to containers. |
| `conditions` | `array` | Output only. The Condition of this Revision, containing its readiness status, and detailed error information in case it did not reach a serving state. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Revision. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `encryptionKeyShutdownDuration` | `string` | If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. |
| `launchStage` | `string` | Set the launch stage to a preview stage on write to allow use of preview features in that stage. On read, describes whether the resource uses preview features. Launch Stages are defined at [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). |
| `observedGeneration` | `string` | Output only. The generation of this Revision currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `annotations` | `object` | KRM-style annotations for the resource. |
| `service` | `string` | Output only. The name of the parent service. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_revisions_get` | `SELECT` | `locationsId, projectsId, revisionsId, servicesId` | Gets information about a Revision. |
| `projects_locations_services_revisions_list` | `SELECT` | `locationsId, projectsId, servicesId` | Lists Revisions from a given Service, or from a given location. |
| `projects_locations_services_revisions_delete` | `DELETE` | `locationsId, projectsId, revisionsId, servicesId` | Deletes a Revision. |
