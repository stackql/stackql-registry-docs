---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
  - result
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.result.results" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_result" /> | `EXEC` | <CopyableCode code="result_handler, endpoint" /> | <CopyableCode code="page" /> | Get result status or the result when it is ready. |


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="page" /> | Number of the page of results to return. The number can range from 0 to the total number of pages minus 1. | `integer` | `0` |

</details>
