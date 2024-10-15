---
title: provider_actions_overview_status
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_actions_overview_status
  - app_compliance_automation
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

Creates, updates, deletes, gets or lists a <code>provider_actions_overview_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_actions_overview_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.provider_actions_overview_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="statusList" /> | `array` | List of different status items. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Get the resource overview status. |

## `SELECT` examples

Get the resource overview status.


```sql
SELECT
statusList
FROM azure_extras.app_compliance_automation.provider_actions_overview_status
;
```