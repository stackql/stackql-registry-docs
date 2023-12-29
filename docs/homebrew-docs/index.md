---
title: homebrew
hide_title: false
hide_table_of_contents: false
keywords:
  - homebrew
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and report on Homebrew packages using SQL
custom_edit_url: null
image: /img/providers/homebrew/stackql-homebrew-provider-featured-image.png
id: homebrew-doc
slug: /providers/homebrew

---
Open-source package manager for macOS and Linux.  
    
:::info Provider Summary (v23.12.00194)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>1</b></span><br />
<span>total methods:&nbsp;<b>1</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>9</b></span><br />
<span>total selectable resources:&nbsp;<b>1</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `homebrew` provider, run the following command:  

```bash
REGISTRY PULL homebrew;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication


> The `homebrew` provider for StackQL supports `SELECT` methods only and does not require any environment variables to be set for authentication.
  
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/homebrew/formula/">formula</a><br />
</div>
<div class="providerDocColumn">
</div>
</div>
