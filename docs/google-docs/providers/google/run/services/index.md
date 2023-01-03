---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The fully qualified name of this Service. In CreateServiceRequest, this field is ignored, and instead composed from CreateServiceRequest.parent and CreateServiceRequest.service_id. Format: projects/{project}/locations/{location}/services/{service_id} |
| `description` | `string` | User-provided description of the Service. This field currently has a 512-character limit. |
| `createTime` | `string` | Output only. The creation time. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `annotations` | `object` | Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run will populate some annotations using 'run.googleapis.com' or 'serving.knative.dev' namespaces. This field follows Kubernetes annotations' namespacing, limits, and rules. More info: https://kubernetes.io/docs/user-guide/annotations |
| `creator` | `string` | Output only. Email address of the authenticated creator. |
| `labels` | `object` | Map of string keys and values that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved. |
| `latestCreatedRevision` | `string` | Output only. Name of the last created revision. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `latestReadyRevision` | `string` | Output only. Name of the latest revision that is serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `observedGeneration` | `string` | Output only. The generation of this Service currently serving traffic. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. Please note that unlike v1, this is an int64 value. As with most Google APIs, its JSON representation will be a `string` instead of an `integer`. |
| `traffic` | `array` | Specifies how to distribute traffic over a collection of Revisions belonging to the Service. If traffic is empty or not provided, defaults to 100% traffic to the latest `Ready` Revision. |
| `ingress` | `string` | Provides the ingress settings for this Service. On output, returns the currently observed ingress settings, or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active. |
| `deleteTime` | `string` | Output only. The deletion time. |
| `template` | `object` | RevisionTemplate describes the data a revision should have when created from a template. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. Please note that unlike v1, this is an int64 value. As with most Google APIs, its JSON representation will be a `string` instead of an `integer`. |
| `reconciling` | `boolean` | Output only. Returns true if the Service is currently being acted upon by the system to bring it into the desired state. When a new Service is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Service to the desired serving state. This process is called reconciliation. While reconciliation is in process, `observed_generation`, `latest_ready_revison`, `traffic_statuses`, and `uri` will have transient values that might mismatch the intended state: Once reconciliation is over (and this field is false), there are two possible outcomes: reconciliation succeeded and the serving state matches the Service, or there was an error, and reconciliation failed. This state can be found in `terminal_condition.state`. If reconciliation succeeded, the following fields will match: `traffic` and `traffic_statuses`, `observed_generation` and `generation`, `latest_ready_revision` and `latest_created_revision`. If reconciliation failed, `traffic_statuses`, `observed_generation`, and `latest_ready_revision` will have the state of the last serving revision, or empty for newly created Services. Additional information on the failure can be found in `terminal_condition` and `conditions`. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. |
| `launchStage` | `string` | The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed. |
| `terminalCondition` | `object` | Defines a status condition for a resource. |
| `uri` | `string` | Output only. The main URI in which this Service is serving traffic. |
| `clientVersion` | `string` | Arbitrary version identifier for the API client. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `lastModifier` | `string` | Output only. Email address of the last authenticated modifier. |
| `uid` | `string` | Output only. Server assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `trafficStatuses` | `array` | Output only. Detailed status information for corresponding traffic targets. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `client` | `string` | Arbitrary identifier for the API client. |
| `binaryAuthorization` | `object` | Settings for Binary Authorization feature. |
| `conditions` | `array` | Output only. The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Service does not reach its Serving state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_get` | `SELECT` | `locationsId, projectsId, servicesId` | Gets information about a Service. |
| `projects_locations_services_list` | `SELECT` | `locationsId, projectsId` | List Services. |
| `projects_locations_services_create` | `INSERT` | `locationsId, projectsId` | Creates a new Service in a given project and location. |
| `projects_locations_services_delete` | `DELETE` | `locationsId, projectsId, servicesId` | Deletes a Service. This will cause the Service to stop serving traffic and will delete all revisions. |
| `projects_locations_services_patch` | `EXEC` | `locationsId, projectsId, servicesId` | Updates a Service. |
