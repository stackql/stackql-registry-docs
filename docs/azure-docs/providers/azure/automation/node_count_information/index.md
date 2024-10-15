---
title: node_count_information
hide_title: false
hide_table_of_contents: false
keywords:
  - node_count_information
  - automation
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

Creates, updates, deletes, gets or lists a <code>node_count_information</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_count_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.node_count_information" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets the name of a count type |
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, countType, resourceGroupName, subscriptionId" /> | Retrieve counts for Dsc Nodes. |

## `SELECT` examples

Retrieve counts for Dsc Nodes.


```sql
SELECT
name,
properties
FROM azure.automation.node_count_information
WHERE automationAccountName = '{{ automationAccountName }}'
AND countType = '{{ countType }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```