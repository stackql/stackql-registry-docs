---
title: formula
hide_title: false
hide_table_of_contents: false
keywords:
  - formula
  - formula
  - homebrew    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and report on Homebrew packages using SQL
custom_edit_url: null
image: /img/providers/homebrew/stackql-homebrew-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>formula</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="homebrew.formula.formula" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the formula. |
| <CopyableCode code="aliases" /> | `array` | Alternative names or aliases for the formula. |
| <CopyableCode code="analytics" /> | `object` | Analytics data related to the formula, such as download counts or build errors.<br /> |
| <CopyableCode code="bottle" /> | `object` | Details about the precompiled binary packages (bottles) for the formula, including URLs and checksums.<br /> |
| <CopyableCode code="build_dependencies" /> | `array` | Dependencies required to build the formula from source.<br /> |
| <CopyableCode code="caveats" /> | `string` | Special instructions or warnings about the formula that users should be aware of.<br /> |
| <CopyableCode code="conflicts_with" /> | `array` | Formula names that conflict with this formula, meaning they cannot be installed simultaneously.<br /> |
| <CopyableCode code="conflicts_with_reasons" /> | `array` | Reasons why the formula conflicts with other formulae.<br /> |
| <CopyableCode code="dependencies" /> | `array` | Dependencies required to run the formula.<br /> |
| <CopyableCode code="deprecated" /> | `boolean` | Whether the formula is deprecated, meaning it is no longer supported or maintained.<br /> |
| <CopyableCode code="deprecation_date" /> | `string` | The date on which the formula was deprecated, if it is deprecated.<br /> |
| <CopyableCode code="deprecation_reason" /> | `string` | The reason why the formula was deprecated, if it is deprecated.<br /> |
| <CopyableCode code="desc" /> | `string` | A short description of the formula.<br /> |
| <CopyableCode code="disable_date" /> | `string` | The date on which the formula was disabled, if it is disabled.<br /> |
| <CopyableCode code="disable_reason" /> | `string` | The reason why the formula was disabled, if it is disabled.<br /> |
| <CopyableCode code="disabled" /> | `boolean` | Whether the formula is disabled, meaning it is not available to install or use.<br /> |
| <CopyableCode code="full_name" /> | `string` | The full, qualified name of the formula including the tap name (if applicable). |
| <CopyableCode code="generated_date" /> | `string` | The date when the formula information was last generated or updated.<br /> |
| <CopyableCode code="head_dependencies" /> | `object` | Dependencies required for installing the HEAD version (directly from the source repository).<br /> |
| <CopyableCode code="homepage" /> | `string` | URL to the formula's homepage or project page.<br /> |
| <CopyableCode code="installed" /> | `array` | Versions of the formula that are currently installed.<br /> |
| <CopyableCode code="keg_only" /> | `boolean` | Whether the formula is keg-only, meaning it is not symlinked into the Homebrew prefix and can be accessed only by its fully qualified name.<br /> |
| <CopyableCode code="keg_only_reason" /> | `string` | The reason why the formula is keg-only, if it is keg-only.<br /> |
| <CopyableCode code="license" /> | `string` | The license under which the formula is distributed.<br /> |
| <CopyableCode code="link_overwrite" /> | `array` | File paths that this formula might request to overwrite during installation.<br /> |
| <CopyableCode code="linked_keg" /> | `string` | The version of the formula that is currently linked into Homebrews prefix.<br /> |
| <CopyableCode code="oldname" /> | `string` | Previous name for the formula, if it was renamed. |
| <CopyableCode code="oldnames" /> | `array` | All previous names the formula had. |
| <CopyableCode code="optional_dependencies" /> | `array` | Dependencies that are optional, meaning they are not required to run the formula.<br /> |
| <CopyableCode code="options" /> | `array` | Options that can be passed to the formula when installing it.<br /> |
| <CopyableCode code="outdated" /> | `boolean` | Whether the formula is outdated, meaning a newer version is available.<br /> |
| <CopyableCode code="pinned" /> | `boolean` | Whether the formula is pinned, meaning it is not upgraded when running `brew upgrade`.<br /> |
| <CopyableCode code="post_install_defined" /> | `boolean` | Whether a post-installation script is defined for the formula.<br /> |
| <CopyableCode code="recommended_dependencies" /> | `array` | Dependencies that are recommended, meaning they are not required to run the formula but are suggested for additional functionality.<br /> |
| <CopyableCode code="requirements" /> | `array` | Non-formula requirements for the formula, such as specific hardware or software conditions.<br /> |
| <CopyableCode code="revision" /> | `integer` | The package revision number, used for versioning beyond the version number.<br /> |
| <CopyableCode code="ruby_source_checksum" /> | `object` | Checksum details for the Ruby source code of the formula.<br /> |
| <CopyableCode code="ruby_source_path" /> | `string` | The file path to the Ruby source code of the formula.<br /> |
| <CopyableCode code="service" /> | `object` | Details if the formula can run as a service or background process.<br /> |
| <CopyableCode code="tap" /> | `string` | The GitHub repository (tap) where the formula is located. |
| <CopyableCode code="tap_git_head" /> | `string` | The latest commit SHA of the tap repository containing the formula.<br /> |
| <CopyableCode code="test_dependencies" /> | `array` | Dependencies required for running the formulas tests.<br /> |
| <CopyableCode code="urls" /> | `object` | URLs related to the formula, such as the source URL.<br /> |
| <CopyableCode code="uses_from_macos" /> | `array` | Dependencies that are provided by macOS, which the formula can use.<br /> |
| <CopyableCode code="uses_from_macos_bounds" /> | `array` | The minimum and maximum macOS versions that the formula can use.<br /> |
| <CopyableCode code="variations" /> | `object` | Different variations of the formula, potentially for different operating systems or configurations.<br /> |
| <CopyableCode code="version_scheme" /> | `integer` | Versioning scheme used by the formula.<br /> |
| <CopyableCode code="versioned_formulae" /> | `array` | Other versions of the formula available as separate formulae. |
| <CopyableCode code="versions" /> | `object` | The version numbers of the formula, including the stable, head, and bottle versions.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_formula" /> | `SELECT` | <CopyableCode code="formula_name" /> |
