---
title: customers_gcp_project_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - customers_gcp_project_deployments
  - sasportal
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

Creates, updates, deletes, gets or lists a <code>customers_gcp_project_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers_gcp_project_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sasportal.customers_gcp_project_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deployments" /> | `array` | Optional. Deployments associated with the GCP project |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_list_gcp_project_deployments" /> | `SELECT` | <CopyableCode code="" /> | Returns a list of SAS deployments associated with current GCP project. Includes whether SAS analytics has been enabled or not. |

## `SELECT` examples

Returns a list of SAS deployments associated with current GCP project. Includes whether SAS analytics has been enabled or not.

```sql
SELECT
deployments
FROM google.sasportal.customers_gcp_project_deployments
;
```
