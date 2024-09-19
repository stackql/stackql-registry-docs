---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - connectors
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

Creates, updates, deletes, gets or lists a <code>actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.connectors.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the action. |
| <CopyableCode code="description" /> | `string` | Brief Description of action |
| <CopyableCode code="displayName" /> | `string` | Display Name of action to be shown on client side |
| <CopyableCode code="inputJsonSchema" /> | `object` | JsonSchema representation of schema metadata |
| <CopyableCode code="inputParameters" /> | `array` | List containing input parameter metadata. |
| <CopyableCode code="resultJsonSchema" /> | `object` | JsonSchema representation of schema metadata |
| <CopyableCode code="resultMetadata" /> | `array` | List containing the metadata of result fields. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionsId, connectionsId, locationsId, projectsId" /> | Gets the schema of the given action. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Gets the schema of all the actions supported by the connector. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="actionsId, connectionsId, locationsId, projectsId" /> | Executes an action with the name specified in the request. The input parameters for executing the action are passed through the body of the ExecuteAction request. |

## `SELECT` examples

Gets the schema of all the actions supported by the connector.

```sql
SELECT
name,
description,
displayName,
inputJsonSchema,
inputParameters,
resultJsonSchema,
resultMetadata
FROM google.connectors.actions
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
