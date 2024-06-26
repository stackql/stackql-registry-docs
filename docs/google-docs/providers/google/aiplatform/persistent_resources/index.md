---
title: persistent_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - persistent_resources
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>persistent_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.persistent_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Resource name of a PersistentResource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the PersistentResource was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. The display name of the PersistentResource. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize PersistentResource. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="network" /> | `string` | Optional. The full name of the Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to peered with Vertex AI to host the persistent resources. For example, `projects/12345/global/networks/myVPC`. [Format](/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/&#123;project&#125;/global/networks/&#123;network&#125;`. Where &#123;project&#125; is a project number, as in `12345`, and &#123;network&#125; is a network name. To specify this field, you must have already [configured VPC Network Peering for Vertex AI](https://cloud.google.com/vertex-ai/docs/general/vpc-peering). If this field is left unspecified, the resources aren't peered with any network. |
| <CopyableCode code="reservedIpRanges" /> | `array` | Optional. A list of names for the reserved IP ranges under the VPC network that can be used for this persistent resource. If set, we will deploy the persistent resource within the provided IP ranges. Otherwise, the persistent resource is deployed to any IP ranges under the provided VPC network. Example: ['vertex-ai-ip-range']. |
| <CopyableCode code="resourcePools" /> | `array` | Required. The spec of the pools of different resources. |
| <CopyableCode code="resourceRuntime" /> | `object` | Persistent Cluster runtime information as output |
| <CopyableCode code="resourceRuntimeSpec" /> | `object` | Configuration for the runtime on a PersistentResource instance, including but not limited to: * Service accounts used to run the workloads. * Whether to make it a dedicated Ray Cluster. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time when the PersistentResource for the first time entered the `RUNNING` state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a Study. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the PersistentResource was most recently updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, persistentResourcesId, projectsId" /> | Gets a PersistentResource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists PersistentResources in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a PersistentResource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, persistentResourcesId, projectsId" /> | Deletes a PersistentResource. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, persistentResourcesId, projectsId" /> | Updates a PersistentResource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists PersistentResources in a Location. |
| <CopyableCode code="reboot" /> | `EXEC` | <CopyableCode code="locationsId, persistentResourcesId, projectsId" /> | Reboots a PersistentResource. |
