---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - saas
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.saas.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource uri |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | saas properties |
| <CopyableCode code="tags" /> | `object` | the resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId" /> | Gets information about the specified operation progress. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets all SaaS app operations. |
| <CopyableCode code="saas_resource_list_access_token" /> | `EXEC` | <CopyableCode code="resourceId" /> | Gets the ISV access token for a SaaS resource. |

## `SELECT` examples

Gets all SaaS app operations.


```sql
SELECT
id,
name,
properties,
tags,
type
FROM azure_extras.saas.operations
;
```