---
title: connectivity_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - connectivity_tests
  - networkmanagement
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
<tr><td><b>Name</b></td><td><code>connectivity_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkmanagement.connectivity_tests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Unique name of the resource using the form: `projects/&#123;project_id&#125;/locations/global/connectivityTests/&#123;test_id&#125;` |
| <CopyableCode code="description" /> | `string` | The user-supplied description of the Connectivity Test. Maximum of 512 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the test was created. |
| <CopyableCode code="destination" /> | `object` | Source or destination of the Connectivity Test. |
| <CopyableCode code="displayName" /> | `string` | Output only. The display name of a Connectivity Test. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user-provided metadata. |
| <CopyableCode code="protocol" /> | `string` | IP Protocol of the test. When not provided, "TCP" is assumed. |
| <CopyableCode code="reachabilityDetails" /> | `object` | Results of the configuration analysis from the last run of the test. |
| <CopyableCode code="relatedProjects" /> | `array` | Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries. |
| <CopyableCode code="source" /> | `object` | Source or destination of the Connectivity Test. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the test's configuration was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectivityTestsId, projectsId" /> | Gets the details of a specific Connectivity Test. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all Connectivity Tests owned by a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new Connectivity Test. After you create a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. If the endpoint specifications in `ConnectivityTest` are invalid (for example, containing non-existent resources in the network, or you don't have read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`. If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of AMBIGUOUS. For more information, see the Connectivity Test documentation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectivityTestsId, projectsId" /> | Deletes a specific `ConnectivityTest`. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists all Connectivity Tests owned by a project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="connectivityTestsId, projectsId" /> | Updates the configuration of an existing `ConnectivityTest`. After you update a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. The Reachability state in the test resource is updated with the new result. If the endpoint specifications in `ConnectivityTest` are invalid (for example, they contain non-existent resources in the network, or the user does not have read permissions to the network configurations of listed projects), then the reachability result returns a value of UNKNOWN. If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of `AMBIGUOUS`. See the documentation in `ConnectivityTest` for for more details. |
| <CopyableCode code="rerun" /> | `EXEC` | <CopyableCode code="connectivityTestsId, projectsId" /> | Rerun an existing `ConnectivityTest`. After the user triggers the rerun, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. Even though the test configuration remains the same, the reachability result may change due to underlying network configuration changes. If the endpoint specifications in `ConnectivityTest` become invalid (for example, specified resources are deleted in the network, or you lost read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`. |
