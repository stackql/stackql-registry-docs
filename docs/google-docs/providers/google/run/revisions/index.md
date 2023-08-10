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
| `logUri` | `string` | Output only. The Google Console URI to obtain logs for the Revision. |
| `labels` | `object` | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. |
| `service` | `string` | Output only. The name of the parent service. |
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `volumes` | `array` | A list of Volumes to make available to containers. |
| `executionEnvironment` | `string` | The execution environment being used to host this Revision. |
| `sessionAffinity` | `boolean` | Enable session affinity. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `createTime` | `string` | Output only. The creation time. |
| `encryptionKeyShutdownDuration` | `string` | If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Revision. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `encryptionKeyRevocationAction` | `string` | The action to take if the encryption key is revoked. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Service.reconciling` for additional information on reconciliation process in Cloud Run. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `timeout` | `string` | Max allowed time for an instance to respond to a request. |
| `containers` | `array` | Holds the single container that defines the unit of execution for this Revision. |
| `scaling` | `object` | Settings for revision-level scaling settings. |
| `annotations` | `object` | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| `serviceAccount` | `string` | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. |
| `launchStage` | `string` | The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA. |
| `observedGeneration` | `string` | Output only. The generation of this Revision currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `maxInstanceRequestConcurrency` | `integer` | Sets the maximum number of requests that each serving instance can receive. |
| `vpcAccess` | `object` | VPC Access settings. For more information on creating a VPC Connector, visit https://cloud.google.com/vpc/docs/configure-serverless-vpc-access For information on how to configure Cloud Run with an existing VPC Connector, visit https://cloud.google.com/run/docs/configuring/connecting-vpc |
| `conditions` | `array` | Output only. The Condition of this Revision, containing its readiness status, and detailed error information in case it did not reach a serving state. |
| `encryptionKey` | `string` | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, revisionsId, servicesId` | Gets information about a Revision. |
| `list` | `SELECT` | `locationsId, projectsId, servicesId` | Lists Revisions from a given Service, or from a given location. |
| `delete` | `DELETE` | `locationsId, projectsId, revisionsId, servicesId` | Deletes a Revision. |
| `_list` | `EXEC` | `locationsId, projectsId, servicesId` | Lists Revisions from a given Service, or from a given location. |
