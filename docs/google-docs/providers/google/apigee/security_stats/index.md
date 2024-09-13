---
title: security_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - security_stats
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

Creates, updates, deletes or gets an <code>security_stat</code> resource or lists <code>security_stats</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.security_stats" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_security_stats_query_tabular_stats" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Retrieve security statistics as tabular rows. |
| <CopyableCode code="organizations_environments_security_stats_query_time_series_stats" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Retrieve security statistics as a collection of time series. |
