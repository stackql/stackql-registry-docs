---
title: provider_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_actions
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

Creates, updates, deletes, gets or lists a <code>provider_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.provider_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="storageAccountList" /> | `array` | The storage account list which in use in related reports. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_in_use_storage_accounts" /> | `SELECT` | <CopyableCode code="" /> | List the storage accounts which are in use by related reports |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="" /> | Check if the given name is available for a report. |
| <CopyableCode code="onboard" /> | `EXEC` | <CopyableCode code="data__subscriptionIds" /> | Onboard given subscriptions to Microsoft.AppComplianceAutomation provider. |
| <CopyableCode code="trigger_evaluation" /> | `EXEC` | <CopyableCode code="data__resourceIds" /> | Trigger quick evaluation for the given subscriptions. |

## `SELECT` examples

List the storage accounts which are in use by related reports


```sql
SELECT
storageAccountList
FROM azure_extras.app_compliance_automation.provider_actions
;
```