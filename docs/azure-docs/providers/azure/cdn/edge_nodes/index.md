---
title: edge_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_nodes
  - cdn
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

Creates, updates, deletes, gets or lists a <code>edge_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.edge_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create an edgenode. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Edgenodes are the global Point of Presence (POP) locations used to deliver CDN content to end users. |

## `SELECT` examples

Edgenodes are the global Point of Presence (POP) locations used to deliver CDN content to end users.


```sql
SELECT
properties
FROM azure.cdn.edge_nodes
;
```