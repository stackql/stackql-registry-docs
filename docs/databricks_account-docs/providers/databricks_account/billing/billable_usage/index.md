---
title: billable_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - billable_usage
  - billing
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>billable_usage</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billable_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.billable_usage" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="account_id, end_month, start_month" /> | Returns billable usage logs in CSV format for the specified account and date range. For the data schema, see |
