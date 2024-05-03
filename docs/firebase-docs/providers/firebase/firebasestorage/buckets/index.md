---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - firebasestorage
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebasestorage.buckets" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_buckets_get" /> | `SELECT` | <CopyableCode code="bucketsId, projectsId" /> | Gets a single linked storage bucket. |
| <CopyableCode code="projects_buckets_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the linked storage buckets for a project. |
