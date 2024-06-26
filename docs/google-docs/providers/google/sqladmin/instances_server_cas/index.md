---
title: instances_server_cas
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_server_cas
  - sqladmin
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
<tr><td><b>Name</b></td><td><code>instances_server_cas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.instances_server_cas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeVersion" /> | `string` |  |
| <CopyableCode code="certs" /> | `array` | List of server CA certificates for the instance. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#instancesListServerCas`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_server_cas" /> | `SELECT` | <CopyableCode code="instance, project" /> |
