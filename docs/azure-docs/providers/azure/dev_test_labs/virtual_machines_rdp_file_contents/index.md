---
title: virtual_machines_rdp_file_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines_rdp_file_contents
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>virtual_machines_rdp_file_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines_rdp_file_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.virtual_machines_rdp_file_contents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contents" /> | `string` | The contents of the .rdp file |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Gets a string that represents the contents of the RDP file for the virtual machine |

## `SELECT` examples

Gets a string that represents the contents of the RDP file for the virtual machine


```sql
SELECT
contents
FROM azure.dev_test_labs.virtual_machines_rdp_file_contents
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```