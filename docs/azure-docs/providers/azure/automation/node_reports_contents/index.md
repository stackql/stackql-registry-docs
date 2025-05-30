---
title: node_reports_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - node_reports_contents
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

Creates, updates, deletes, gets or lists a <code>node_reports_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_reports_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.node_reports_contents" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeId, reportId, resourceGroupName, subscriptionId" /> | Retrieve the Dsc node reports by node id and report id. |

## `SELECT` examples

Retrieve the Dsc node reports by node id and report id.


```sql
SELECT

FROM azure.automation.node_reports_contents
WHERE automationAccountName = '{{ automationAccountName }}'
AND nodeId = '{{ nodeId }}'
AND reportId = '{{ reportId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```