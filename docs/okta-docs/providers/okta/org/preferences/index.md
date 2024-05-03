---
title: preferences
hide_title: false
hide_table_of_contents: false
keywords:
  - preferences
  - org
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>preferences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.org.preferences" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="showEndUserFooter" /> | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subdomain" /> | Gets preferences of your organization. |
| <CopyableCode code="hideEndUserFooter" /> | `EXEC` | <CopyableCode code="subdomain" /> | Hide the Okta UI footer for all end users of your organization. |
| <CopyableCode code="showEndUserFooter" /> | `EXEC` | <CopyableCode code="subdomain" /> | Makes the Okta UI footer visible for all end users of your organization. |
