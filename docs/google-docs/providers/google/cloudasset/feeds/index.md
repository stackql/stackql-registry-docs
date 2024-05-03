---
title: feeds
hide_title: false
hide_table_of_contents: false
keywords:
  - feeds
  - cloudasset
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudasset.feeds" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Gets details about an asset feed. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists all asset feeds in a parent project/folder/organization. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a feed in a parent project/folder/organization to listen to its asset updates. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name" /> | Deletes an asset feed. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="name" /> | Updates an asset feed configuration. |
