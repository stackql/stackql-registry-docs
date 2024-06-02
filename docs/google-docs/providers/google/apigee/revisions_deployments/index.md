---
title: revisions_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions_deployments
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.revisions_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiProxy" /> | `string` | API proxy. |
| <CopyableCode code="deployStartTime" /> | `string` | Time the API proxy was marked `deployed` in the control plane in millisconds since epoch. |
| <CopyableCode code="environment" /> | `string` | Environment. |
| <CopyableCode code="errors" /> | `array` | Errors reported for this deployment. Populated only when state == ERROR. **Note**: This field is displayed only when viewing deployment status. |
| <CopyableCode code="instances" /> | `array` | Status reported by each runtime instance. **Note**: This field is displayed only when viewing deployment status. |
| <CopyableCode code="pods" /> | `array` | Status reported by runtime pods. **Note**: **This field is deprecated**. Runtime versions 1.3 and above report instance level status rather than pod status. |
| <CopyableCode code="proxyDeploymentType" /> | `string` | Output only. The type of the deployment (standard or extensible) Deployed proxy revision will be marked as extensible in following 2 cases. 1. The deployed proxy revision uses extensible policies. 2. If a environment supports flowhooks and flow hook is configured. |
| <CopyableCode code="revision" /> | `string` | API proxy revision. |
| <CopyableCode code="routeConflicts" /> | `array` | Conflicts in the desired state routing configuration. The presence of conflicts does not cause the state to be `ERROR`, but it will mean that some of the deployment's base paths are not routed to its environment. If the conflicts change, the state will transition to `PROGRESSING` until the latest configuration is rolled out to all instances. **Note**: This field is displayed only when viewing deployment status. |
| <CopyableCode code="serviceAccount" /> | `string` | The full resource name of Cloud IAM Service Account that this deployment is using, eg, `projects/-/serviceAccounts/&#123;email&#125;`. |
| <CopyableCode code="state" /> | `string` | Current state of the deployment. **Note**: This field is displayed only when viewing deployment status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_apis_revisions_get_deployments" /> | `SELECT` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Gets the deployment of an API proxy revision and actual state reported by runtime pods. |
| <CopyableCode code="organizations_environments_sharedflows_revisions_get_deployments" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, revisionsId, sharedflowsId" /> | Gets the deployment of a shared flow revision and actual state reported by runtime pods. |
