---
title: host_security_reports_result_view
hide_title: false
hide_table_of_contents: false
keywords:
  - host_security_reports_result_view
  - apigee
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

Creates, updates, deletes or gets an <code>host_security_reports_result_view</code> resource or lists <code>host_security_reports_result_view</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_security_reports_result_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.host_security_reports_result_view" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `integer` | Error code when there is a failure. |
| <CopyableCode code="error" /> | `string` | Error message when there is a failure. |
| <CopyableCode code="metadata" /> | `object` | Metadata for the security report. |
| <CopyableCode code="rows" /> | `array` | Rows of security report result. Each row is a JSON object. Example: {sum(message_count): 1, developer_app: "(not set)",…} |
| <CopyableCode code="state" /> | `string` | State of retrieving ResultView. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_host_security_reports_get_result_view" /> | `SELECT` | <CopyableCode code="hostSecurityReportsId, organizationsId" /> | After the query is completed, use this API to view the query result when result size is small. |

## `SELECT` examples

After the query is completed, use this API to view the query result when result size is small.

```sql
SELECT
code,
error,
metadata,
rows,
state
FROM google.apigee.host_security_reports_result_view
WHERE hostSecurityReportsId = '{{ hostSecurityReportsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
