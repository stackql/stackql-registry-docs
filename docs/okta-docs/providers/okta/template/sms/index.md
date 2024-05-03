---
title: sms
hide_title: false
hide_table_of_contents: false
keywords:
  - sms
  - template
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
<tr><td><b>Name</b></td><td><code>sms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.template.sms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="template" /> | `string` |
| <CopyableCode code="translations" /> | `object` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="templateId, subdomain" /> | Fetches a specific template by `id` |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Adds a new custom SMS template to your organization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="templateId, subdomain" /> | Removes an SMS template. |
| <CopyableCode code="partialUpdate" /> | `EXEC` | <CopyableCode code="templateId, subdomain" /> | Updates only some of the SMS template properties: |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="templateId, subdomain" /> | Updates the SMS template. |
