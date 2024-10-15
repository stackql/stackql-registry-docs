---
title: executes
hide_title: false
hide_table_of_contents: false
keywords:
  - executes
  - mysql
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

Creates, updates, deletes, gets or lists a <code>executes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.executes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="privateDnsZoneSuffix" /> | `string` | Represents the private DNS zone suffix. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Get private DNS zone suffix in the cloud. |

## `SELECT` examples

Get private DNS zone suffix in the cloud.


```sql
SELECT
privateDnsZoneSuffix
FROM azure.mysql.executes
;
```