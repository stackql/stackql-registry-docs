---
title: revisions__deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions__deployments
  - apigee
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
<tr><td><b>Name</b></td><td><code>revisions__deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.revisions__deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `serviceAccount` | `string` | The full resource name of Cloud IAM Service Account that this deployment is using, eg, `projects/-/serviceAccounts/&#123;email&#125;`. |
| `routeConflicts` | `array` | Conflicts in the desired state routing configuration. The presence of conflicts does not cause the state to be `ERROR`, but it will mean that some of the deployment's base paths are not routed to its environment. If the conflicts change, the state will transition to `PROGRESSING` until the latest configuration is rolled out to all instances. **Note**: This field is displayed only when viewing deployment status. |
| `apiProxy` | `string` | API proxy. |
| `deployStartTime` | `string` | Time the API proxy was marked `deployed` in the control plane in millisconds since epoch. |
| `errors` | `array` | Errors reported for this deployment. Populated only when state == ERROR. **Note**: This field is displayed only when viewing deployment status. |
| `instances` | `array` | Status reported by each runtime instance. **Note**: This field is displayed only when viewing deployment status. |
| `environment` | `string` | Environment. |
| `pods` | `array` | Status reported by runtime pods. **Note**: **This field is deprecated**. Runtime versions 1.3 and above report instance level status rather than pod status. |
| `revision` | `string` | API proxy revision. |
| `state` | `string` | Current state of the deployment. **Note**: This field is displayed only when viewing deployment status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_apis_revisions_getDeployments` | `SELECT` | `apisId, environmentsId, organizationsId, revisionsId` | Gets the deployment of an API proxy revision and actual state reported by runtime pods. |
| `organizations_environments_sharedflows_revisions_getDeployments` | `SELECT` | `environmentsId, organizationsId, revisionsId, sharedflowsId` | Gets the deployment of a shared flow revision and actual state reported by runtime pods. |
