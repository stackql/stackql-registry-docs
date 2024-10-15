---
title: report_scoping_questions
hide_title: false
hide_table_of_contents: false
keywords:
  - report_scoping_questions
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

Creates, updates, deletes, gets or lists a <code>report_scoping_questions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_scoping_questions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.report_scoping_questions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="questions" /> | `array` | List of scoping questions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName" /> | Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed. |

## `SELECT` examples

Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed.


```sql
SELECT
questions
FROM azure_extras.app_compliance_automation.report_scoping_questions
WHERE reportName = '{{ reportName }}';
```