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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>formula</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>homebrew.formula.formula</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the formula. |
| `aliases` | `array` | Alternative names or aliases for the formula. |
| `analytics` | `object` | Analytics data related to the formula, such as download counts or build errors.<br /> |
| `bottle` | `object` | Details about the precompiled binary packages (bottles) for the formula, including URLs and checksums.<br /> |
| `build_dependencies` | `array` | Dependencies required to build the formula from source.<br /> |
| `caveats` | `string` | Special instructions or warnings about the formula that users should be aware of.<br /> |
| `conflicts_with` | `array` | Formula names that conflict with this formula, meaning they cannot be installed simultaneously.<br /> |
| `conflicts_with_reasons` | `array` | Reasons why the formula conflicts with other formulae.<br /> |
| `dependencies` | `array` | Dependencies required to run the formula.<br /> |
| `deprecated` | `boolean` | Whether the formula is deprecated, meaning it is no longer supported or maintained.<br /> |
| `deprecation_date` | `string` | The date on which the formula was deprecated, if it is deprecated.<br /> |
| `deprecation_reason` | `string` | The reason why the formula was deprecated, if it is deprecated.<br /> |
| `desc` | `string` | A short description of the formula.<br /> |
| `disable_date` | `string` | The date on which the formula was disabled, if it is disabled.<br /> |
| `disable_reason` | `string` | The reason why the formula was disabled, if it is disabled.<br /> |
| `disabled` | `boolean` | Whether the formula is disabled, meaning it is not available to install or use.<br /> |
| `full_name` | `string` | The full, qualified name of the formula including the tap name (if applicable). |
| `generated_date` | `string` | The date when the formula information was last generated or updated.<br /> |
| `head_dependencies` | `object` | Dependencies required for installing the HEAD version (directly from the source repository).<br /> |
| `homepage` | `string` | URL to the formula's homepage or project page.<br /> |
| `installed` | `array` | Versions of the formula that are currently installed.<br /> |
| `keg_only` | `boolean` | Whether the formula is keg-only, meaning it is not symlinked into the Homebrew prefix and can be accessed only by its fully qualified name.<br /> |
| `keg_only_reason` | `string` | The reason why the formula is keg-only, if it is keg-only.<br /> |
| `license` | `string` | The license under which the formula is distributed.<br /> |
| `link_overwrite` | `array` | File paths that this formula might request to overwrite during installation.<br /> |
| `linked_keg` | `string` | The version of the formula that is currently linked into Homebrews prefix.<br /> |
| `oldname` | `string` | Previous name for the formula, if it was renamed. |
| `oldnames` | `array` | All previous names the formula had. |
| `optional_dependencies` | `array` | Dependencies that are optional, meaning they are not required to run the formula.<br /> |
| `options` | `array` | Options that can be passed to the formula when installing it.<br /> |
| `outdated` | `boolean` | Whether the formula is outdated, meaning a newer version is available.<br /> |
| `pinned` | `boolean` | Whether the formula is pinned, meaning it is not upgraded when running `brew upgrade`.<br /> |
| `post_install_defined` | `boolean` | Whether a post-installation script is defined for the formula.<br /> |
| `recommended_dependencies` | `array` | Dependencies that are recommended, meaning they are not required to run the formula but are suggested for additional functionality.<br /> |
| `requirements` | `array` | Non-formula requirements for the formula, such as specific hardware or software conditions.<br /> |
| `revision` | `integer` | The package revision number, used for versioning beyond the version number.<br /> |
| `ruby_source_checksum` | `object` | Checksum details for the Ruby source code of the formula.<br /> |
| `ruby_source_path` | `string` | The file path to the Ruby source code of the formula.<br /> |
| `service` | `object` | Details if the formula can run as a service or background process.<br /> |
| `tap` | `string` | The GitHub repository (tap) where the formula is located. |
| `tap_git_head` | `string` | The latest commit SHA of the tap repository containing the formula.<br /> |
| `test_dependencies` | `array` | Dependencies required for running the formulas tests.<br /> |
| `urls` | `object` | URLs related to the formula, such as the source URL.<br /> |
| `uses_from_macos` | `array` | Dependencies that are provided by macOS, which the formula can use.<br /> |
| `uses_from_macos_bounds` | `array` | The minimum and maximum macOS versions that the formula can use.<br /> |
| `variations` | `object` | Different variations of the formula, potentially for different operating systems or configurations.<br /> |
| `version_scheme` | `integer` | Versioning scheme used by the formula.<br /> |
| `versioned_formulae` | `array` | Other versions of the formula available as separate formulae. |
| `versions` | `object` | The version numbers of the formula, including the stable, head, and bottle versions.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_formula` | `SELECT` | `formula_name` |
