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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `scaling` | `object` | Settings for revision-level scaling settings. |
| `launchStage` | `string` | Set the launch stage to a preview stage on write to allow use of preview features in that stage. On read, describes whether the resource uses preview features. Launch Stages are defined at [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). |
| `uid` | `string` | Output only. Server assigned unique identifier for the Revision. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `deleteTime` | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| `reconciling` | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Service.reconciling` for additional information on reconciliation process in Cloud Run. |
| `createTime` | `string` | Output only. The creation time. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `encryptionKey` | `string` | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
| `volumes` | `array` | A list of Volumes to make available to containers. |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved. |
| `conditions` | `array` | Output only. The Condition of this Revision, containing its readiness status, and detailed error information in case it did not reach a serving state. |
| `annotations` | `object` | KRM-style annotations for the resource. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `vpcAccess` | `object` | VPC Access settings. For more information on creating a VPC Connector, visit https://cloud.google.com/vpc/docs/configure-serverless-vpc-access For information on how to configure Cloud Run with an existing VPC Connector, visit https://cloud.google.com/run/docs/configuring/connecting-vpc |
| `executionEnvironment` | `string` | The execution environment being used to host this Revision. |
| `service` | `string` | Output only. The name of the parent service. |
| `containers` | `array` | Holds the single container that defines the unit of execution for this Revision. |
| `timeout` | `string` | Max allowed time for an instance to respond to a request. |
| `serviceAccount` | `string` | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. |
| `logUri` | `string` | Output only. The Google Console URI to obtain logs for the Revision. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| `observedGeneration` | `string` | Output only. The generation of this Revision currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `maxInstanceRequestConcurrency` | `integer` | Sets the maximum number of requests that each serving instance can receive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_revisions_get` | `SELECT` | `locationsId, projectsId, revisionsId, servicesId` | Gets information about a Revision. |
| `projects_locations_services_revisions_list` | `SELECT` | `locationsId, projectsId, servicesId` | List Revisions from a given Service, or from a given location. |
| `projects_locations_services_revisions_delete` | `DELETE` | `locationsId, projectsId, revisionsId, servicesId` | Delete a Revision. |
