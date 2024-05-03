---
title: lfs
hide_title: false
hide_table_of_contents: false
keywords:
  - lfs
  - migrations
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.migrations.lfs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="oid" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="ref_name" /> | `string` |
| <CopyableCode code="size" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_large_files" /> | `SELECT` | <CopyableCode code="owner, repo" /> | List files larger than 100MB found during the import<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API.<br /> |
| <CopyableCode code="set_lfs_preference" /> | `EXEC` | <CopyableCode code="owner, repo, data__use_lfs" /> | You can import repositories from Subversion, Mercurial, and TFS that include files larger than 100MB. This ability<br />is powered by [Git LFS](https://git-lfs.com).<br /><br />You can learn more about our LFS feature and working with large files [on our help<br />site](https://docs.github.com/repositories/working-with-files/managing-large-files).<br /><br />**Warning:** Support for importing Mercurial, Subversion and Team Foundation Version Control repositories will end<br />on October 17, 2023. For more details, see [changelog](https://gh.io/github-importer-non-git-eol). In the coming weeks, we will update<br />these docs to reflect relevant changes to the API and will contact all integrators using the "Source imports" API.<br /> |
