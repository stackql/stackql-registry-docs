---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - lke
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.versions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLKEVersion" /> | `SELECT` | <CopyableCode code="version" /> | View a Kubernetes version available for deployment to a Kubernetes cluster.<br /> |
| <CopyableCode code="getLKEVersions" /> | `SELECT` |  | List the Kubernetes versions available for deployment to a Kubernetes cluster.<br /> |
| <CopyableCode code="_getLKEVersion" /> | `EXEC` | <CopyableCode code="version" /> | View a Kubernetes version available for deployment to a Kubernetes cluster.<br /> |
| <CopyableCode code="_getLKEVersions" /> | `EXEC` |  | List the Kubernetes versions available for deployment to a Kubernetes cluster.<br /> |
