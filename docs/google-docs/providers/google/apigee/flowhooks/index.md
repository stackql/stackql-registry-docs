---
title: flowhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - flowhooks
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>flowhooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flowhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.flowhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Description of the flow hook. |
| <CopyableCode code="continueOnError" /> | `boolean` | Optional. Flag that specifies whether execution should continue if the flow hook throws an exception. Set to `true` to continue execution. Set to `false` to stop execution if the flow hook throws an exception. Defaults to `true`. |
| <CopyableCode code="flowHookPoint" /> | `string` | Output only. Where in the API call flow the flow hook is invoked. Must be one of `PreProxyFlowHook`, `PostProxyFlowHook`, `PreTargetFlowHook`, or `PostTargetFlowHook`. |
| <CopyableCode code="sharedFlow" /> | `string` | Shared flow attached to this flow hook, or empty if there is none attached. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_flowhooks_get" /> | `SELECT` | <CopyableCode code="environmentsId, flowhooksId, organizationsId" /> | Returns the name of the shared flow attached to the specified flow hook. If there's no shared flow attached to the flow hook, the API does not return an error; it simply does not return a name in the response. |
| <CopyableCode code="organizations_environments_flowhooks_attach_shared_flow_to_flow_hook" /> | `EXEC` | <CopyableCode code="environmentsId, flowhooksId, organizationsId" /> | Attaches a shared flow to a flow hook. |
| <CopyableCode code="organizations_environments_flowhooks_detach_shared_flow_from_flow_hook" /> | `EXEC` | <CopyableCode code="environmentsId, flowhooksId, organizationsId" /> | Detaches a shared flow from a flow hook. |

## `SELECT` examples

Returns the name of the shared flow attached to the specified flow hook. If there's no shared flow attached to the flow hook, the API does not return an error; it simply does not return a name in the response.

```sql
SELECT
description,
continueOnError,
flowHookPoint,
sharedFlow
FROM google.apigee.flowhooks
WHERE environmentsId = '{{ environmentsId }}'
AND flowhooksId = '{{ flowhooksId }}'
AND organizationsId = '{{ organizationsId }}';
```
