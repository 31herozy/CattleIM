package com.example.thinkpad.cattleim.frags.search;

import com.example.common.app.BaseFragment;
import com.example.thinkpad.cattleim.R;
import com.example.thinkpad.cattleim.activities.SearchActivity;

public class SearchGroupFragment extends BaseFragment implements SearchActivity.SearchFragment {
    public static final String TAG = "找群";

    @Override
    public void search(String content) {

    }

    @Override
    protected int getContentLayoutId() {
        return R.layout.hello;
    }
}
